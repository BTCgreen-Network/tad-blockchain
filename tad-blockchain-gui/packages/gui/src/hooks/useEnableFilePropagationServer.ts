import { useLocalStorage } from '@tad/api-react';

export default function useEnableFilePropagationServer() {
  return useLocalStorage<boolean>('enableFilePropagationServer', false);
}
