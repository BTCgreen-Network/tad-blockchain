import BigNumber from 'bignumber.js';

import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function tadToMojo(tad: string | number | BigNumber): BigNumber {
  return tadFormatter(tad, Unit.TAD).to(Unit.MOJO).toBigNumber();
}
