import { useCallback } from 'react';
import type { NFTInfo } from '@tad/api';
import { useHiddenList } from '@tad/core';

export default function useHiddenNFTs() {
  const [isNFTHidden, setIsNFTHidden, hiddenNFTs] =
    useHiddenList<NFTInfo['$nftId']>('nfts');

  const handleSetIsHidden = useCallback(
    (nft: NFTInfo, isHidden: boolean) => {
      setIsNFTHidden(nft.$nftId, isHidden);
    },
    [setIsNFTHidden],
  );

  const handleIsNFTHidden = useCallback(
    (nft: NFTInfo) => isNFTHidden(nft?.$nftId),
    [isNFTHidden],
  );

  return [handleIsNFTHidden, handleSetIsHidden, hiddenNFTs];
}
