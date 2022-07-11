import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function mojoToCAT(mojo: string | number | BigNumber): BigNumber {
  return tadFormatter(mojo, Unit.MOJO)
    .to(Unit.CAT)
    .toBigNumber();
}