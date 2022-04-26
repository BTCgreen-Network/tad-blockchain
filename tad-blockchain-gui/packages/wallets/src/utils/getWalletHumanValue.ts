import type { Wallet } from '@tad/api';
import { WalletType } from '@tad/api';
import { mojoToCATLocaleString, mojoToTadLocaleString } from '@tad/core';

export default function getWalletHumanValue(wallet: Wallet, value: number): string {
  return wallet.type === WalletType.CAT
    ? mojoToCATLocaleString(value)
    : mojoToTadLocaleString(value);
}
