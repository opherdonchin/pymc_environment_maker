# -*- coding: utf-8 -*-
import pymc as pm
import arviz as az
import numpy as np
import matplotlib.pyplot as plt

def generate_data(seed=42, mu=5, sigma=1, size=100):
    np.random.seed(seed)
    return np.random.normal(loc=mu, scale=sigma, size=size)

def define_model(data):
    with pm.Model() as model:
        mu = pm.Normal("mu", mu=0, sigma=10)
        sigma = pm.HalfNormal("sigma", sigma=5)
        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)
    return model

def sample(model, draws=2000, tune=1000):
    with model:
        idata = pm.sample(draws=draws, tune=tune)
    return idata

def display_posterior(idata):
    az.plot_posterior(idata, var_names=["mu", "sigma"], hdi_prob=0.94)
    plt.show()

if __name__ == "__main__":
    data = generate_data()
    model = define_model(data)
    idata = sample(model)
    display_posterior(idata)
