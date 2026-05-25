#ifndef STORAGE_VOLUMES_H
#define STORAGE_VOLUMES_H

enum {
  VOLUME_SENSOR_SAMPLES, 
};

#endif
#if defined(VS)
VS(VOLUME_SENSOR_SAMPLES, 1024)
#undef VS
#endif
#if defined(VB)
VB(VOLUME_SENSOR_SAMPLES, 0)
#undef VB
#endif
