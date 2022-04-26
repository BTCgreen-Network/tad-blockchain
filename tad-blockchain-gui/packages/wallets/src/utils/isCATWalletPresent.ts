import type { Wallet, CATToken } from '@tad/api';
import { WalletType } from '@tad/api';

export default function isCATWalletPresent(wallets: Wallet[], token: CATToken): boolean {
  return !!wallets?.find((wallet) => {
    if (wallet.type === WalletType.CAT && wallet.meta?.assetId === token.assetId) {
      return true;
    }

    return false;
  });
}
