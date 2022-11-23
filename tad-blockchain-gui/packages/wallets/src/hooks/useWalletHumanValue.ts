import type { Wallet } from '@tad/api';
import { WalletType } from '@tad/api';
import { mojoToCATLocaleString, mojoToTadLocaleString, useLocale } from '@tad/core';
import BigNumber from 'bignumber.js';
import { useMemo } from 'react';

export default function useWalletHumanValue(
  wallet: Wallet,
  value?: string | number | BigNumber,
  unit?: string
): string {
  const [locale] = useLocale();

  return useMemo(() => {
    if (wallet && value !== undefined) {
      const localisedValue =
        wallet.type === WalletType.CAT ? mojoToCATLocaleString(value, locale) : mojoToTadLocaleString(value, locale);

      return `${localisedValue} ${unit}`;
    }

    return '';
  }, [wallet, value, unit, locale]);
}
