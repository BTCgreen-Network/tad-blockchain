import { useLocalStorage } from '@tad/api-react';

export default function useHideObjectionableContent() {
  return useLocalStorage<boolean>('hideObjectionableContent', true);
}
