import ChildProcess from 'child_process';

export function runWalletCommandWithArgs(commandArgs: string[]): string {
  const command = 'tad';
  const args = ['wallet', ...commandArgs];
  const cli = `${command} ${args.join(' ')}`;

  console.log(`Running CLI: ${cli}`);
  const child = ChildProcess.spawnSync(command, args, { stdio: 'pipe' });
  const output = child.stdout.toString();

  return output;
}

export function isWalletSynced(fingerprint: string | number) {
  const output = runWalletCommandWithArgs(['show', '--fingerprint', fingerprint.toString()]);
  // console.log(`stdout: ${output}`);

  // Regular expression to check output for "Sync Status:"
  const match = output.match(/Sync status:\s(.+)\n/);
  // console.log(`Matched sync status ? ${match?.[1] ?? ''}`);
  const isSynced = match && match[1] === 'Synced';
  console.log(`Synced ? ${isSynced}`);

  return isSynced;
}

export function getWalletBalance(fingerprint: string | number): string | undefined {
  const output = runWalletCommandWithArgs(['show', '--fingerprint', fingerprint.toString()]);

  const balanceMatch = output.match(/Tad Wallet:\s+-Total Balance:\s+([^\s]+)/);
  const balance = balanceMatch?.[1];
  return balance;
}

export function stopAllTad() {
  const command = 'tad';
  ChildProcess.spawnSync(command, ['stop', 'all', '-d'], { stdio: 'pipe' });
  console.log(command);
}