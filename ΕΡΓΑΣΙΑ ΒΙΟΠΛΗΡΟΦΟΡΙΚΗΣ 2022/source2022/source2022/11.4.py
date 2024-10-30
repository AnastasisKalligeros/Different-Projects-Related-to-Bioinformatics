states = ('a','b')

emission_probability = {
	'a': {'A':0.4, 'G':0.4, 'T':0.1, 'C':0.1},
	'b': {'T':0.3, 'C':0.3, 'A':0.2, 'G':0.2},
}

observations = ('G', 'G', 'C', 'T')

start_probability = { 'a': 0.5,'b': 0.5 }

transition_probability = {
    'a': {'a':0.9, 'b':0.1},
	'b': {'a':0.1, 'b':0.9}
    
}

def viterbi(observations, states, start_probability, transition_probability, emission_probability):
    
    trellis = [{}]
    
    path = {}
    maxx =0
    maxx_state = 'a'
  
    for state in states:
        trellis[0][state] = start_probability[state] * emission_probability[state][observations[0]]
        path[state] = [state]
        if trellis[0][state] > maxx:
            maxx = trellis[0][state]
            maxx_state = state

    
    for observations_index in range(1,len(observations)):
       
        trellis.append({})
        new_path = {}

        for state in states:
           
          
            (probability, possible_state) = max(
            [(trellis[observations_index-1][maxx_state] * transition_probability[maxx_state][state] 
            * emission_probability[state][observations[observations_index]],state)])

            print (probability,possible_state)

            trellis[observations_index][state] = probability
            
            new_path[state] = path[possible_state] + [state]

        path = new_path

   
    (probability, state) = max([(trellis[len(observations) - 1][state], state) for state in states])
       
    return (probability, path[state])

print(viterbi(observations, states, start_probability, transition_probability, emission_probability))

