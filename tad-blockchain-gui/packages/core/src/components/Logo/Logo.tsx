import { Tad } from '@tad/icons';
import { Box, BoxProps } from '@mui/material';
import React from 'react';
import styled from 'styled-components';

const StyledTad = styled(Tad)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledTad />
    </Box>
  );
}
