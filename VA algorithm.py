
class ValueAverage:

    def __init__(self,initial_value,investment_frequency,input_increase_rate,project_value_growth_rate,goal):
        self.initial_value=initial_value
        self.investment_frequency=investment_frequency

        self.input_increase_rate=input_increase_rate
        self.project_value_growth_rate=project_value_growth_rate
        self.goal=goal

    def calculate_base_input(self):
        input_increase_rate=self.input_increase_rate
        project_value_growth_rate=self.project_value_growth_rate
        if input_increase_rate==project_value_growth_rate:
            base_input=self.calculate_base_input_samerate()
            return base_input
        elif input_increase_rate<project_value_growth_rate:
            base_input=self.calculate_base_input_different_rate()
            return base_input
        else:
            print('error')

    def calculate_base_input_samerate(self):
        initial_value=self.initial_value
        investment_frequency=self.investment_frequency
        input_increase_rate=self.input_increase_rate
        project_value_growth_rate=self.project_value_growth_rate
        goal=self.goal


        growth_coeffcient=1+project_value_growth_rate
        input_increase_coefficent=1+input_increase_rate

        final_growth_rate=growth_coeffcient**(investment_frequency-1)
        final_increase_rate=input_increase_coefficent**investment_frequency

        #simple version


        PartA=goal/final_growth_rate
        PartB=PartA-initial_value

        base_input=PartB/(investment_frequency)
        return base_input

    '''
    initial value calculation problem              already done for one senario
    increase rate calulation problem
    
    calculation part solved
    first time, already have initial value, so put the base value into the market immediately 
    
    
    still have some problem in condition
    
    '''

    def calculate_base_input_different_rate(self):
        initial_value=self.initial_value
        investment_frequency=self.investment_frequency
        input_increase_rate=self.input_increase_rate
        project_value_growth_rate=self.project_value_growth_rate
        goal=self.goal

        '''
        (I+B)^n+c*B=goal
        c is a known constant

        the algorithm to find the proper base input could be improved
        '''
        ref_base_input=int(self.calculate_base_input_samerate())
        exit_flag=False
        for base_input in range(-goal,goal):
            initial_value = self.initial_value
            targetValue = initial_value+base_input
            for i in range(0, self.investment_frequency+1):
                base_input_rate = (self.input_increase_rate + 1) ** (i+1)
                if targetValue > goal:
                    exit_flag=True

                    break
                targetValue = targetValue * (self.project_value_growth_rate + 1) + base_input * base_input_rate
            if exit_flag:
                break
        return base_input



    '''
    if the initial value could reach the goal, then the equation just does not work
    '''
    def display_target_value(self):
        base_input=self.calculate_base_input()

        print('base_input is ',base_input)

        initial_value=self.initial_value
        targetValue =initial_value+base_input
        for i in range(0,self.investment_frequency+1):
            base_input_rate=(self.input_increase_rate+1)**(i+1)
            print('investment round is ', i + 1, ', target value is ', targetValue)
            targetValue=targetValue*(self.project_value_growth_rate+1)+base_input*base_input_rate




            #print('investment round is ',i+1,', target value is ',targetValue)



a=ValueAverage(initial_value=2250,investment_frequency=12,input_increase_rate=0.005,project_value_growth_rate=0.02,goal=32000)
a.display_target_value()

