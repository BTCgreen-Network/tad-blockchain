import PlotterName from './PlotterName';
import optionsForPlotter from '../utils/optionsForPlotter';
import defaultsForPlotter from '../utils/defaultsForPlotter';

export default {
  displayName: 'Tad Proof of Space',
  options: optionsForPlotter(PlotterName.TADPOS),
  defaults: defaultsForPlotter(PlotterName.TADPOS),
  installInfo: { installed: true },
};
