import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function catToMojo(cat: string | number | BigNumber): BigNumber {
  return tadFormatter(cat, Unit.CAT)
    .to(Unit.MOJO)
    .toBigNumber();
}