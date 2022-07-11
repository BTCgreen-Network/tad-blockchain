import { WalletType } from '@tad/api';
import type { Wallet } from '@tad/api';

export default function getWalletPrimaryTitle(wallet: Wallet): string {
  switch (wallet.type) {
    case WalletType.STANDARD_WALLET:
      return 'Tad';
    default:
      return wallet.name;
  }
}
