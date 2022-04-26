import Big from 'big.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function tadToMojo(tad: string | number | Big): number {
  return tadFormatter(tad, Unit.TAD)
    .to(Unit.MOJO)
    .toNumber();
}