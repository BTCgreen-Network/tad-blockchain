import Big from 'big.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function catToMojo(cat: string | number | Big): number {
  return tadFormatter(cat, Unit.CAT)
    .to(Unit.MOJO)
    .toNumber();
}