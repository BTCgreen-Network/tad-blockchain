import { type WalletType } from '@tad/api';
import type BigNumber from 'bignumber.js';

type OfferRowData = {
  amount: string;
  assetWalletId: number; // 0 if no selection made
  walletType: WalletType;
};

export default OfferRowData;
