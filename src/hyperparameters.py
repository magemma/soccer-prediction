params = {
    'mlp': {
        'type': 'categorical',
        'params': [
            {
                'activation': ['relu', 'logistic', 'tanh'], 
                'hidden_layer_sizes': [(5,2), (10,5)]
            }
        ],
    },
    'svc': {
        'type': 'categorical',
        'params': [
            {
                'kernel': ['rbf'], 
                'gamma': [1e-3, 1e-4], 
                'C': [1, 10, 100, 1000]
            },
            {
                'kernel': ['linear'], 
                'C': [1, 10, 100, 1000]
            }
        ],
    }
}
