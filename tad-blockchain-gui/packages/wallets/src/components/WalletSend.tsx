import React from 'react';
import { Trans, t } from '@lingui/macro';
import {
  useGetSyncStatusQuery,
  useSendTransactionMutation,
  useFarmBlockMutation,
} from '@tad/api-react';
import {
  Amount,
  ButtonLoading,
  Fee,
  Form,
  TextField,
  Flex,
  Card,
  useOpenDialog,
  tadToMojo,
  getTransactionResult,
  useIsSimulator,
  TooltipIcon,
} from '@tad/core';
import isNumeric from 'validator/es/lib/isNumeric';
import { useForm, useWatch } from 'react-hook-form';
import {
  Button,
  Grid,
  Typography,
} from '@mui/material';
import useWallet from '../hooks/useWallet';
import CreateWalletSendTransactionResultDialog from './WalletSendTransactionResultDialog';

type SendCardProps = {
  walletId: number;
};

type SendTransactionData = {
  address: string;
  amount: string;
  fee: string;
};

export default function WalletSend(props: SendCardProps) {
  const { walletId } = props;

  const isSimulator = useIsSimulator();
  const openDialog = useOpenDialog();
  const [sendTransaction, { isLoading: isSendTransactionLoading }] = useSendTransactionMutation();
  const [farmBlock] = useFarmBlockMutation();
  const methods = useForm<SendTransactionData>({
    defaultValues: {
      address: '',
      amount: '',
      fee: '',
    },
  });

  const addressValue = useWatch<string>({
    control: methods.control,
    name: 'address',
  });

  const { data: walletState, isLoading: isWalletSyncLoading } = useGetSyncStatusQuery({}, {
    pollingInterval: 10000,
  });

  const { wallet } = useWallet(walletId);

  if (!wallet || isWalletSyncLoading) {
    return null;
  }

  const syncing = !!walletState?.syncing;

  async function farm() {
    if (addressValue) {
      await farmBlock({
        address: addressValue,
      }).unwrap();
    }
  }

  async function handleSubmit(data: SendTransactionData) {
    if (isSendTransactionLoading) {
      return;
    }

    if (syncing) {
      throw new Error(t`Please finish syncing before making a transaction`);
    }

    const amount = data.amount.trim();
    if (!isNumeric(amount)) {
      throw new Error(t`Please enter a valid numeric amount`);
    }

    const fee = data.fee.trim() || '0';
    if (!isNumeric(fee)) {
      throw new Error(t`Please enter a valid numeric fee`);
    }

    let address = data.address;
    if (address.includes('colour')) {
      throw new Error(t`Cannot send tad to coloured address. Please enter a tad address.`);
    }

    if (address.slice(0, 12) === 'tad_addr://') {
      address = address.slice(12);
    }
    if (address.startsWith('0x') || address.startsWith('0X')) {
      address = address.slice(2);
    }

    const response = await sendTransaction({
      walletId,
      address,
      amount: tadToMojo(amount),
      fee: tadToMojo(fee),
      waitForConfirmation: true,
    }).unwrap();

    const result = getTransactionResult(response.transaction);
    const resultDialog = CreateWalletSendTransactionResultDialog({success: result.success, message: result.message});

    if (resultDialog) {
      await openDialog(resultDialog);
    }
    else {
      throw new Error(result.message ?? 'Something went wrong');
    }

    methods.reset();
  }

  return (
    <Form methods={methods} onSubmit={handleSubmit}>
      <Flex gap={2} flexDirection="column">
        <Typography variant="h6">
          <Trans>Create Transaction</Trans>
          &nbsp;
          <TooltipIcon>
            <Trans>
              On average there is one minute between each transaction block. Unless
              there is congestion you can expect your transaction to be included in
              less than a minute.
            </Trans>
          </TooltipIcon>
        </Typography>
        <Card>
          <Grid spacing={2} container>
            <Grid xs={12} item>
              <TextField
                name="address"
                variant="filled"
                color="secondary"
                fullWidth
                label={<Trans>Address / Puzzle hash</Trans>}
                required
              />
            </Grid>
            <Grid xs={12} md={6} item>
              <Amount
                id="filled-secondary"
                variant="filled"
                color="secondary"
                name="amount"
                label={<Trans>Amount</Trans>}
                required
                fullWidth
              />
            </Grid>
            <Grid xs={12} md={6} item>
              <Fee
                id="filled-secondary"
                variant="filled"
                name="fee"
                color="secondary"
                label={<Trans>Fee</Trans>}
                fullWidth
              />
            </Grid>
          </Grid>
        </Card>
        <Flex justifyContent="flex-end" gap={1}>
          {isSimulator && (
            <Button onClick={farm} variant="outlined">
              <Trans>Farm</Trans>
            </Button>
          )}

          <ButtonLoading
            variant="contained"
            color="primary"
            type="submit"
            loading={isSendTransactionLoading}
          >
            <Trans>Send</Trans>
          </ButtonLoading>
        </Flex>
      </Flex>
    </Form>
  );
}
