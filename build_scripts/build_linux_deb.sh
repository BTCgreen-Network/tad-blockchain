#!/bin/bash

set -o errexit

if [ ! "$1" ]; then
  echo "This script requires either amd64 of arm64 as an argument"
	exit 1
elif [ "$1" = "amd64" ]; then
	PLATFORM="$1"
	DIR_NAME="tad-blockchain-linux-x64"
else
	PLATFORM="$1"
	DIR_NAME="tad-blockchain-linux-arm64"
fi
export PLATFORM

# If the env variable NOTARIZE and the username and password variables are
# set, this will attempt to Notarize the signed DMG

if [ ! "$TAD_INSTALLER_VERSION" ]; then
	echo "WARNING: No environment variable TAD_INSTALLER_VERSION set. Using 0.0.0."
	TAD_INSTALLER_VERSION="0.0.0"
fi
echo "Tad Installer Version is: $TAD_INSTALLER_VERSION"
export TAD_INSTALLER_VERSION

echo "Installing npm and electron packagers"
cd npm_linux_deb || exit
npm install
PATH=$(npm bin):$PATH
cd .. || exit

echo "Create dist/"
rm -rf dist
mkdir dist

echo "Create executables with pyinstaller"
SPEC_FILE=$(python -c 'import tad; print(tad.PYINSTALLER_SPEC_PATH)')
pyinstaller --log-level=INFO "$SPEC_FILE"
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "pyinstaller failed!"
	exit $LAST_EXIT_CODE
fi

# Builds CLI only .deb
# need j2 for templating the control file
pip install j2cli
CLI_DEB_BASE="tad-blockchain-cli_$TAD_INSTALLER_VERSION-1_$PLATFORM"
mkdir -p "dist/$CLI_DEB_BASE/opt/tad"
mkdir -p "dist/$CLI_DEB_BASE/usr/bin"
mkdir -p "dist/$CLI_DEB_BASE/DEBIAN"
j2 -o "dist/$CLI_DEB_BASE/DEBIAN/control" assets/deb/control.j2
cp -r dist/daemon/* "dist/$CLI_DEB_BASE/opt/tad/"
ln -s ../../opt/tad/tad "dist/$CLI_DEB_BASE/usr/bin/tad"
dpkg-deb --build --root-owner-group "dist/$CLI_DEB_BASE"
# CLI only .deb done

cp -r dist/daemon ../tad-blockchain-gui/packages/gui
cd .. || exit
cd tad-blockchain-gui || exit

echo "npm build"
lerna clean -y
npm install
# Audit fix does not currently work with Lerna. See https://github.com/lerna/lerna/issues/1663
# npm audit fix
npm run build
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "npm run build failed!"
	exit $LAST_EXIT_CODE
fi

# Change to the gui package
cd packages/gui || exit

# sets the version for tad-blockchain in package.json
cp package.json package.json.orig
jq --arg VER "$TAD_INSTALLER_VERSION" '.version=$VER' package.json > temp.json && mv temp.json package.json

electron-packager . tad-blockchain --asar.unpack="**/daemon/**" --platform=linux \
--icon=src/assets/img/Tad.icns --overwrite --app-bundle-id=net.tad.blockchain \
--appVersion=$TAD_INSTALLER_VERSION --executable-name=tad-blockchain
LAST_EXIT_CODE=$?

# reset the package.json to the original
mv package.json.orig package.json

if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "electron-packager failed!"
	exit $LAST_EXIT_CODE
fi

mv $DIR_NAME ../../../build_scripts/dist/
cd ../../../build_scripts || exit

echo "Create tad-$TAD_INSTALLER_VERSION.deb"
rm -rf final_installer
mkdir final_installer
electron-installer-debian --src "dist/$DIR_NAME/" \
  --arch "$PLATFORM" \
  --options.version "$TAD_INSTALLER_VERSION" \
  --config deb-options.json
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "electron-installer-debian failed!"
	exit $LAST_EXIT_CODE
fi

# Move the cli only deb into final installers as well, so it gets uploaded as an artifact
mv "dist/$CLI_DEB_BASE.deb" final_installer/

ls final_installer/
