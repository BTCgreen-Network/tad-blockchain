import { useGetNFTsByNFTIDsQuery, useLocalStorage } from '@tad/api-react';

export default function useNachoNFTs() {
  const [nachoNFTsString] = useLocalStorage('nachoNFTs', '');
  const nachoNFTIDs = nachoNFTsString.split(',').map((nachoNFT: string) => nachoNFT.trim());

  return useGetNFTsByNFTIDsQuery({ nftIds: nachoNFTIDs }, { skip: !nachoNFTsString || nachoNFTIDs.length === 0 });
}
