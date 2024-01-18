class RemoteControl:
  def __init__(self):
    self.__volume = 60
    self.__channel = 3
    self.__total_channels = 5
  
  def get_volume(self):
    return self.__volume

  def get_channel(self):
    return self.__channel
  
  def set_upper_channel(self):
    if self.__channel < self.__total_channels:
      self.__channel += 1
    else:
      self.__channel = 1
    
    return self.__channel
  
  def set_lower_channel(self):
    if self.__channel > 1:
      self.__channel -= 1
    else:
      self.__channel = self.__total_channels

    return self.__channel

control = RemoteControl()
print(control.get_volume()) 
print(control.get_channel()) 
print(control.set_upper_channel()) 
print(control.set_upper_channel()) 
print(control.set_upper_channel()) 
