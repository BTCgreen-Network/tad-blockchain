import React from 'react';
import { SvgIcon, SvgIconProps } from '@mui/material';
import TadIcon from './images/tad_logo.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={TadIcon} viewBox="0 0 150 58" {...props} />;
}
