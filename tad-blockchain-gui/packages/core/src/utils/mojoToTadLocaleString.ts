import Big from 'big.js';
import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function mojoToTadLocaleString(mojo: string | number | Big) {
  return tadFormatter(Number(mojo), Unit.MOJO)
    .to(Unit.TAD)
    .toLocaleString();
}