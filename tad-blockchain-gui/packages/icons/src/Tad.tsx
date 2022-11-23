import { SvgIcon, SvgIconProps } from '@mui/material';
import React from 'react';

import TadIcon from './images/tad.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={TadIcon} viewBox="0 0 150 58" {...props} />;
}
