import Big from 'big.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function mojoToCAT(mojo: string | number | Big): number {
  return tadFormatter(mojo, Unit.MOJO)
    .to(Unit.CAT)
    .toNumber();
}