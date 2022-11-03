import { useGetNFTsByNFTIDsQuery } from '@tad/api-react';
import { useLocalStorage } from '@tad/core';

export default function useNachoNFTs() {
  const [nachoNFTsString] = useLocalStorage('nachoNFTs', '');
  const nachoNFTIDs = nachoNFTsString
    .split(',')
    .map((nachoNFT: string) => nachoNFT.trim());

  return useGetNFTsByNFTIDsQuery(
    { nftIds: nachoNFTIDs },
    { skip: !nachoNFTsString || nachoNFTIDs.length === 0 },
  );
}
