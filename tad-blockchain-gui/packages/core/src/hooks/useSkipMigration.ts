import { useLocalStorage } from '@tad/api-react';

export default function useSkipMigration(): [boolean, (skip: boolean) => void] {
  const [skip, setSkip] = useLocalStorage<boolean>('skipMigration', false);

  return [skip, setSkip];
}
