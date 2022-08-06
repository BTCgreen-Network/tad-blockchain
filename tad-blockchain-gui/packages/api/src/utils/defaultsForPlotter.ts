import PlotterName from '../constants/PlotterName';
import { PlotterDefaults } from '../@types/Plotter';
import { bladebitDefaults, madmaxDefaults, tadposDefaults } from '../constants/Plotters';

export default function defaultsForPlotter(plotterName: PlotterName): PlotterDefaults {
  switch (plotterName) {
    case PlotterName.BLADEBIT:
      return bladebitDefaults;
    case PlotterName.MADMAX:
      return madmaxDefaults;
    case PlotterName.TADPOS: // fallthrough
    default:
      return tadposDefaults;
  }
}
