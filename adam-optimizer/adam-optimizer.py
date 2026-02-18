import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m = beta1*np.array(m) + (1-beta1)*np.array(grad)
    v = beta2*np.array(v) + (1-beta2)*(np.square(grad))

    mt1 = m/(1-beta1**t)
    vt1 = v/(1-beta2**t)

    theta = param - lr*(mt1/(np.sqrt(vt1) + eps))

    return theta, m, v
    pass