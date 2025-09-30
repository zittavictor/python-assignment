class Walk:
    
    def __init__(self, walker_name, num_steps, step_length):
        self._walker_name = walker_name
        self._num_steps = num_steps
        self._step_length = step_length
    
    @property
    def walker_name(self):
        return self._walker_name
    
    @walker_name.setter
    def walker_name(self, value):
        self._walker_name = value
    
    @property
    def num_steps(self):
        return self._num_steps
    
    @num_steps.setter
    def num_steps(self, value):
        self._num_steps = value
    
    @property
    def step_length(self):
        return self._step_length
    
    @step_length.setter
    def step_length(self, value):
        self._step_length = value
    
    def calculate_miles(self):
        INCHES_PER_MILE = 63360
        miles = (self._num_steps * self._step_length) / INCHES_PER_MILE
        return miles
