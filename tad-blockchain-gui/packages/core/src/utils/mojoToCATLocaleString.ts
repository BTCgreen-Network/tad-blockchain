import BigNumber from 'bignumber.js';

import Unit from '../constants/Unit';
import tadFormatter from './tadFormatter';

export default function mojoToCATLocaleString(mojo: string | number | BigNumber, locale?: string) {
  return tadFormatter(mojo, Unit.MOJO).to(Unit.CAT).toLocaleString(locale);
}
