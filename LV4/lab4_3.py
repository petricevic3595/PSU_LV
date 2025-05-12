import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

# Generiranje podataka
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# Podjela podataka
np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:]

xtrain_base = x[indeksi_train]
ytrain = y_measured[indeksi_train]

xtest_base = x[indeksi_test]
ytest = y_measured[indeksi_test]

# Inicijalizacija
stupnjevi = [2, 6, 15]
MSEtrain = []
MSEtest = []

plt.figure(1)
plt.plot(x, y_true, 'k--', label='pozadinska funkcija')

for deg in stupnjevi:
    poly = PolynomialFeatures(degree=deg)
    
    xtrain = poly.fit_transform(xtrain_base)
    xtest = poly.transform(xtest_base)
    xnew = poly.transform(x)
    
    linearModel = lm.LinearRegression()
    linearModel.fit(xtrain, ytrain)
    
    ytrain_p = linearModel.predict(xtrain)
    ytest_p = linearModel.predict(xtest)
    
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    MSEtest.append(mean_squared_error(ytest, ytest_p))
    
    y_model = linearModel.predict(xnew)
    plt.plot(x, y_model, label='stupanj ' + str(deg))


plt.plot(xtrain_base, ytrain, 'ok', label='train')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Modeli za različite stupnjeve i pozadinska funkcija')
plt.legend(loc=4)
plt.grid(True)
plt.show()


print("MSEtrain =", MSEtrain)
print("MSEtest  =", MSEtest)

#MSEtrain = [0.7579630147780275, 0.19556471929761512, 0.16349452609858914
#MSEtest  = [1.274508388745306, 0.31157034276778534, 0.43156333016617665]

#sto vise smanjimo degree varijablu to ce nasa tocnost biti manja