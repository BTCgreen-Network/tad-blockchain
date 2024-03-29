import type { Plot } from '@tad/api';
import { useDeletePlotMutation } from '@tad/api-react';
import { ConfirmDialog, More, MenuItem, useOpenDialog } from '@tad/core';
import { Trans } from '@lingui/macro';
import { DeleteForever as DeleteForeverIcon } from '@mui/icons-material';
import { ListItemIcon, Typography } from '@mui/material';
import React from 'react';

export type PlotActionProps = {
  plot: Plot;
};

export default function PlotAction(props: PlotActionProps) {
  const {
    plot: { filename },
  } = props;

  const openDialog = useOpenDialog();
  const [deletePlot] = useDeletePlotMutation();

  async function handleDeletePlot() {
    await openDialog(
      <ConfirmDialog
        title={<Trans>Delete Plot</Trans>}
        confirmTitle={<Trans>Delete</Trans>}
        confirmColor="danger"
        onConfirm={() => deletePlot({ filename }).unwrap()}
      >
        <Trans>Are you sure you want to delete the plot? The plot cannot be recovered.</Trans>
      </ConfirmDialog>
    );
  }

  return (
    <More>
      <MenuItem onClick={handleDeletePlot} close>
        <ListItemIcon>
          <DeleteForeverIcon fontSize="small" />
        </ListItemIcon>
        <Typography variant="inherit" noWrap>
          <Trans>Delete</Trans>
        </Typography>
      </MenuItem>
    </More>
  );
}
