import math


def get_vol_reg(config, v_line, polarity, turns_ratio, z,r02, x02):

  vr = None

  if config == ['d', 'd', 'd']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),((v_ph_sec[1])-(z[1]))]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])
  elif config == ['d', 'd', 'y']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [0.577*(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),((v_ph_sec[1])-(z[1])-30)]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])

  elif config == ['y', 'y', 'd']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [0.577*(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),((v_ph_sec[1])-(z[1])+30)]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])

  elif config == ['y', 'y', 'y']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [0.577*(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),((v_ph_sec[1])-(z[1]))]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])

  elif config == ['d', 'y', 'd']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [1.732*(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),-((v_ph_sec[1])-(z[1]))]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])

  elif config == ['d', 'y', 'd']:
    v_ph_sec=[(v_line[0]), ((v_line[1])+polarity*30)]
    i_ph= [(v_ph_sec[0])/(z[0])*(turns_ratio[1]/turns_ratio[0]),-((v_ph_sec[1])-(z[1]))]
    phi=v_ph_sec[1]-i_ph[1]
    vr= float(i_ph[0])*(((float(r02)*float(math.cos(phi*(math.pi)/180))))+(float(x02)*float(math.sin(phi*(math.pi)/180))))/float(turns_ratio[1])

  return vr