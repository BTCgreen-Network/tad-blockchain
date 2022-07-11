import { useMemo } from 'react';
import type { Wallet } from '@tad/api';
import { WalletType } from '@tad/api';
import { useGetWalletsQuery, useGetWalletBalanceQuery } from '@tad/api-react';

export default function useStandardWallet(): {
  loading: boolean;
  wallet?: Wallet;
  balance?: number;
} {
  const { data: wallets, isLoading: isLoadingGetWallets } =
    useGetWalletsQuery();
  const { data: balance, isLoading: isLoadingWalletBalance } =
    useGetWalletBalanceQuery({
      walletId: 1,
    });

  const isLoading = isLoadingGetWallets || isLoadingWalletBalance;

  const wallet = useMemo(() => {
    return wallets?.find((item) => item?.type === WalletType.STANDARD_WALLET);
  }, [wallets]);

  return {
    loading: isLoading,
    wallet,
    balance: balance?.confirmedWalletBalance,
  };
}
