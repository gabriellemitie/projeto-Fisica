from math import*
from math import sqrt
import matplotlib.pyplot #biblioteca para gerar os graficos solicitados


tempo =[0,
0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1,1.02,1.04,1.06,1.08,1.1,1.12,1.14,1.16,1.18,1.2,1.22,1.24,1.26,1.28,1.3,1.32,1.34,1.36,1.38,1.4,1.42,1.44,1.46,1.48,1.5,1.52,1.54,1.56,1.58,1.6,1.62,1.64,1.66,1.68,1.7,1.72,1.74,1.76,1.78,1.8,1.82,1.84,1.86,1.88,1.9,1.92,1.94,1.96,1.98,2,2.02,2.04,2.06,2.08,2.1,2.12,2.14,2.16,2.18,2.2,2.22,2.24,2.26,2.28,2.3,2.32,2.34,2.36,2.38,2.4,2.42,2.44,2.46,2.48,2.5,2.52,2.54,2.56,2.58,2.6,2.62,2.64,2.66,2.68,2.7,2.72,2.74,2.76,2.78,2.8,2.82,2.84,2.86,2.88,2.9,2.92,2.94,2.96,2.98,3,3.02,3.04,3.06,3.08,3.1,3.12,3.14,3.16,3.18,3.2,3.22,3.24,3.26,3.28,3.3,3.32,3.34,3.36,3.38,3.4,3.42,3.44,3.46,3.48,3.5,3.52,3.54,3.56,3.58,3.6,3.62,3.64,3.66,3.68,3.7,3.72,3.74,3.76,3.78,3.8,3.82,3.84,7.16,7.18,7.2,7.22,7.24,7.26,7.28,7.3,7.32,7.34,7.36,7.38,7.4,7.42,7.44,7.46,7.48,7.5,7.52,7.54,7.56,7.58,7.6,7.62,7.64,7.66,7.68,7.7,7.72,7.74,7.76,7.78,7.8,7.82,7.84,7.86,7.88,7.9,7.92,7.94,7.96,7.98,8,8.02,8.04,8.06,8.08,8.1,8.12,8.14,8.16,8.18,8.2,8.22,8.24,8.26,8.28,8.3,8.32,8.34,8.36,8.38,8.4,8.42,8.44,8.46,8.48,8.5,8.52,8.54,8.56,8.58,8.6,8.62,8.64,8.66,8.68,8.7,8.72,8.74,8.76,8.78,8.8,8.82,8.84,8.86,8.88,8.9,8.92,8.94,8.96,8.98,9,9.02,9.04,9.06,9.08,9.1,9.12,9.14,9.16,9.18,9.2,9.22,9.24,9.26,9.28,9.3,9.32,9.34,9.36,9.38,9.4]

PosicaoXBola = [1,
1.044,1.088,1.131,1.175,1.218,1.262,1.305,1.348,1.39,1.433,1.476,1.518,1.56,1.602,1.644,1.686,1.728,1.77,1.811,1.852,1.893,1.934,1.975,2.016,2.057,2.097,2.137,2.177,2.217,2.257,2.297,2.336,2.376,2.415,2.454,2.493,2.532,2.57,2.609,2.647,2.685,2.723,2.761,2.799,2.836,2.874,2.911,2.948,2.985,3.022,3.059,3.095,3.131,3.168,3.204,3.24,3.275,3.311,3.346,3.381,3.416,3.451,3.486,3.521,3.555,3.589,3.623,3.657,3.691,3.725,3.758,3.792,3.825,3.858,3.891,3.923,3.956,3.988,4.02,4.052,4.084,4.115,4.147,4.178,4.209,4.24,4.271,4.302,4.332,4.363,4.393,4.423,4.452,4.482,4.511,4.541,4.57,4.599,4.627,4.656,4.684,4.713,4.741,4.769,4.796,4.824,4.851,4.878,4.905,4.932,4.959,4.985,5.011,5.037,5.063,5.089,5.115,5.14,5.165,5.19,5.215,5.24,5.264,5.288,5.313,5.336,5.36,5.384,5.407,5.43,5.453,5.476,5.499,5.521,5.543,5.565,5.587,5.609,5.63,5.652,5.673,5.694,5.714,5.735,5.755,5.775,5.795,5.815,5.835,5.854,5.873,5.892,5.911,5.93,5.948,5.966,5.984,6.002,6.02,6.037,6.054,6.071,6.088,6.105,6.121,6.137,6.153,6.169,6.185,6.2,6.216,6.231,6.245,6.26,6.275,6.289,6.303,6.317,6.33,6.344,6.357,6.37,6.383,6.395,6.407,6.42,6.432,6.443,6.455,6.466,6.477,6.48,5.1,5.071,5.041,5.011,4.981,4.95,4.92,4.889,4.857,4.826,4.794,4.761,4.729,4.696,4.663,4.63,4.596,4.563,4.528,4.494,4.459,4.424,4.389,4.353,4.318,4.282,4.245,4.208,4.171,4.134,4.097,4.059,4.021,3.982,3.944,3.905,3.866,3.826,3.786,3.746,3.706,3.665,3.624,3.583,3.541,3.499,3.457,3.415,3.372,3.329,3.286,3.242,3.198,3.154,3.11,3.065,3.02,2.974,2.929,2.883,2.837,2.79,2.743,2.696,2.649,2.601,2.553,2.505,2.456,2.407,2.358,2.308,2.258,2.208,2.158,2.107,2.056,2.005,1.953,1.901,1.849,1.796,1.743,1.69,1.637,1.583,1.529,1.475,1.42,1.365,1.31,1.254,1.198,1.142,1.085,1.028,0.971,0.914,0.856,0.798,0.739,0.681,0.622,0.562,0.503,0.443,0.382,0.322,0.261,0.2,0.138,0.076,0.014]

PosicaoYBola =[0.5,
0.544,0.588,0.631,0.675,0.718,0.761,0.804,0.847,0.89,0.932,0.974,1.016,1.058,1.1,1.142,1.184,1.225,1.266,1.307,1.348,1.389,1.429,1.47,1.51,1.55,1.59,1.63,1.669,1.709,1.748,1.787,1.826,1.865,1.904,1.942,1.98,2.018,2.056,2.094,2.132,2.17,2.207,2.244,2.281,2.318,2.355,2.391,2.428,2.464,2.5,2.536,2.572,2.607,2.643,2.678,2.713,2.748,2.783,2.818,2.852,2.886,2.92,2.954,2.988,3.022,3.056,3.089,3.122,3.155,3.188,3.221,3.253,3.286,3.318,3.35,3.382,3.414,3.445,3.477,3.508,3.539,3.57,3.601,3.632,3.662,3.692,3.722,3.752,3.782,3.812,3.842,3.871,3.9,3.929,3.958,3.987,4.015,4.044,4.072,4.1,4.128,4.156,4.183,4.211,4.238,4.265,4.292,4.319,4.346,4.372,4.398,4.424,4.45,4.476,4.502,4.528,4.553,4.578,4.603,4.628,4.653,4.677,4.702,4.726,4.75,4.774,4.798,4.821,4.845,4.868,4.891,4.914,4.937,4.96,4.982,5.004,5.026,5.048,5.07,5.092,5.114,5.135,5.156,5.177,5.198,5.219,5.239,5.26,5.28,5.3,5.32,5.34,5.359,5.379,5.398,5.417,5.436,5.455,5.474,5.492,5.51,5.528,5.546,5.564,5.582,5.6,5.617,5.634,5.651,5.668,5.685,5.701,5.718,5.734,5.75,5.766,5.782,5.797,5.813,5.828,5.843,5.858,5.873,5.888,5.902,5.916,5.93,5.944,5.958,5.972,5.986,5.999,5.999,5.986,5.972,5.958,5.944,5.93,5.916,5.902,5.888,5.873,5.858,5.843,5.828,5.813,5.797,5.782,5.766,5.75,5.734,5.718,5.701,5.685,5.668,5.651,5.634,5.617,5.6,5.582,5.564,5.546,5.528,5.51,5.492,5.474,5.455,5.436,5.417,5.398,5.379,5.359,5.34,5.32,5.3,5.28,5.26,5.239,5.219,5.198,5.177,5.156,5.135,5.114,5.092,5.07,5.048,5.026,5.004,4.982,4.96,4.937,4.914,4.891,4.868,4.845,4.821,4.798,4.774,4.75,4.726,4.702,4.677,4.653,4.628,4.603,4.578,4.553,4.528,4.502,4.476,4.45,4.424,4.398,4.372,4.346,4.319,4.292,4.265,4.238,4.211,4.183,4.156,4.128,4.1,4.072,4.044,4.015,3.987,3.958,3.929,3.9,3.871,3.842,3.812,3.782,3.752,3.722,3.692,3.662,3.632,3.601,3.57,3.539,3.508]

CopiaTempo = tempo.copy()
CopiaPosicaoXBola = PosicaoXBola.copy()
CopiaPosicaoYBola = PosicaoYBola.copy()

VelocidadeXBola = [2.8632,2.851012,2.838824,2.826636,2.814448,2.80226,2.790072, 2.777884, 2.765696,2.753508,2.74132,2.729132,2.716944,2.704756,2.692568,2.68038,2.668192,2.656004,2.643816,2.631628,2.61944,2.607252,2.595064,2.582876,2.570688,2.5585,2.546312,2.534124,2.521936,2.509748,2.49756,2.485372,2.473184,2.460996,2.448808,2.43662,2.424432,2.412244,2.400056,2.387868,2.37568,2.363492,2.351304,2.339116,2.326928,2.31474,2.302552,2.290364,2.278176,2.265988,2.2538,2.241612,2.229424,2.217236,2.205048,2.19286,2.180672,2.168484,2.156296,2.144108,2.13192,2.119732,2.107544,2.095356,2.083168,2.07098,2.058792,2.046604,2.034416,2.022228,2.01004,1.997852,1.985664,1.973476,1.961288,1.9491,1.936912,1.924724,1.912536,1.900348,1.88816,1.875972,1.863784,1.851596,1.839408,1.82722,1.815032,1.802844,1.790656,1.778468,1.76628,1.754092,1.741904,1.729716,1.717528,1.70534,1.693152,1.680964,1.668776,1.656588,1.6444,1.632212,1.620024,1.607836,1.595648,1.58346,1.571272,1.559084,1.546896,1.534708,1.52252,1.510332,1.498144,1.485956,1.473768,1.46158,1.449392,1.437204,1.425016,1.412828,1.40064,1.388452,1.376264,1.364076,1.351888,1.3397,1.327512,1.315324,1.303136,1.290948,1.27876,1.266572,1.254384,1.242196,1.230008,1.21782,1.205632,1.193444,1.181256,1.169068,1.15688,1.144692,1.132504,1.120316,1.108128,1.09594,1.083752,1.071564,1.059376,1.047188,1.035,1.022812,1.010624,0.998436,0.986248,0.97406,0.961872,0.949684,0.937496,0.925308,0.91312,0.900932,0.888744,0.876556,0.864368,0.85218,0.839992,0.827804,0.815616,0.803428,0.79124,0.779052,0.766864,0.754676,0.742488,0.7303,0.718112,0.705924,0.693736,0.681548,0.66936,0.657172,0.644984,0.632796,0.620608,0.60842,0.596232,0.584044,0.571856,0.559668,0.54748,0.535292,0.523104,-1.500104,-1.512292,-1.52448,-1.536668,-1.548856,-1.561044,-1.573232,-1.58542,-1.597608,-1.609796,-1.621984,-1.634172,-1.64636,-1.658548,-1.670736,-1.682924,-1.695112,-1.7073,-1.719488,-1.731676,-1.743864,-1.756052,-1.76824,-1.780428,-1.792616,-1.804804,-1.816992,-1.82918,-1.841368,-1.853556,-1.865744,-1.877932,-1.89012,-1.902308,-1.914496,-1.926684,-1.938872,-1.95106,-1.963248,-1.975436,-1.987624,-1.999812,-2.012,-2.024188,-2.036376,-2.048564,-2.060752,-2.07294,-2.085128,-2.097316,-2.109504,-2.121692,-2.13388,-2.146068,-2.158256,-2.170444,-2.182632,-2.19482,-2.207008,-2.219196,-2.231384,-2.243572,-2.25576,-2.267948,-2.280136,-2.292324,-2.304512,-2.3167,-2.328888,-2.341076,-2.353264,-2.365452,-2.37764,-2.389828,-2.402016,-2.414204,-2.426392,-2.43858,-2.450768,-2.462956,-2.475144,-2.487332,-2.49952,-2.511708,-2.523896,-2.536084,-2.548272,-2.56046,-2.572648,-2.584836,-2.597024,-2.609212,-2.6214,-2.633588,-2.645776,-2.657964,-2.670152,-2.68234,-2.694528,-2.706716,-2.718904,-2.731092,-2.74328,-2.755468,-2.767656,-2.779844,-2.792032,-2.80422,-2.816408,-2.828596,-2.840784,-2.852972,-2.86516]
VelocidadeYBola = [2.4096,2.400828,2.392056,2.383284,2.374512,2.36574,2.356968,2.348196,2.339424,2.330652,2.32188,2.313108,2.304336,2.295564,2.286792,2.27802,2.269248,2.260476,2.251704,2.242932,2.23416,2.225388,2.216616,2.207844,2.199072,2.1903,2.181528,2.172756,2.163984,2.155212,2.14644,2.137668,2.128896,2.120124,2.111352,2.10258,2.093808,2.085036,2.076264,2.067492,2.05872,2.049948,2.041176,2.032404,2.023632,2.01486,2.006088,1.997316,1.988544,1.979772,1.971,1.962228,1.953456,1.944684,1.935912,1.92714,1.918368,1.909596,1.900824,1.892052,1.88328,1.874508,1.865736,1.856964,1.848192,1.83942,1.830648,1.821876,1.813104,1.804332,1.79556,1.786788,1.778016,1.769244,1.760472,1.7517,1.742928,1.734156,1.725384,1.716612,1.70784,1.699068,1.690296,1.681524,1.672752,1.66398,1.655208,1.646436,1.637664,1.628892,1.62012,1.611348,1.602576,1.593804,1.585032,1.57626,1.567488,1.558716,1.549944,1.541172,1.5324,1.523628,1.514856,1.506084,1.497312,1.48854,1.479768,1.470996,1.462224,1.453452,1.44468,1.435908,1.427136,1.418364,1.409592,1.40082,1.392048,1.383276,1.374504,1.365732,1.35696,1.348188,1.339416,1.330644,1.321872,1.3131,1.304328,1.295556,1.286784,1.278012,1.26924,1.260468,1.251696,1.242924,1.234152,1.22538,1.216608,1.207836,1.199064,1.190292,1.18152,1.172748,1.163976,1.155204,1.146432,1.13766,1.128888,1.120116,1.111344,1.102572,1.0938,1.085028,1.076256,1.067484,1.058712,1.04994,1.041168,1.032396,1.023624,1.014852,1.00608,0.997308,0.988536,0.979764,0.970992,0.96222,0.953448,0.944676,0.935904,0.927132,0.91836,0.909588,0.900816,0.892044,0.883272,0.8745,0.865728,0.856956,0.848184,0.839412,0.83064,0.821868,0.813096,0.804324,0.795552,0.78678,0.778008,0.769236,0.760464,0.751692,0.74292,0.734148,0.725376,-0.730776,-0.739548,-0.74832,-0.757092,-0.765864,-0.774636,-0.783408,-0.79218,-0.800952,-0.809724,-0.818496,-0.827268,-0.83604,-0.844812,-0.853584,-0.862356,-0.871128,-0.8799,-0.888672,-0.897444,-0.906216,-0.914988,-0.92376,-0.932532,-0.941304,-0.950076,-0.958848,-0.96762,-0.976392,-0.985164,-0.993936,-1.002708,-1.01148,-1.020252,-1.029024,-1.037796,-1.046568,-1.05534,-1.064112,-1.072884,-1.081656,-1.090428,-1.0992,-1.107972,-1.116744,-1.125516,-1.134288,-1.14306,-1.151832,-1.160604,-1.169376,-1.178148,-1.18692,-1.195692,-1.204464,-1.213236,-1.222008,-1.23078,-1.239552,-1.248324,-1.257096,-1.265868,-1.27464,-1.283412,-1.292184,-1.300956,-1.309728,-1.3185,-1.327272,-1.336044,-1.344816,-1.353588,-1.36236,-1.371132,-1.379904,-1.388676,-1.397448,-1.40622,-1.414992,-1.423764,-1.432536,-1.441308,-1.45008,-1.458852,-1.467624,-1.476396,-1.485168,-1.49394,-1.502712,-1.511484,-1.520256,-1.529028,-1.5378,-1.546572,-1.555344,-1.564116,-1.572888,-1.58166,-1.590432,-1.599204,-1.607976,-1.616748,-1.62552,-1.634292,-1.643064,-1.651836,-1.660608,-1.66938,-1.678152,-1.686924,-1.695696,-1.704468,-1.7132]
CopiaVelocidadeXBola = VelocidadeXBola.copy()
CopiaVelocidadeYBola = VelocidadeYBola.copy()
AceleracaoXBola = []
AceleracaoYBola = []
pontosAbolaX = -0.6094
pontosAbolaY = -0.4386

for o in range(0, len(VelocidadeXBola)):
  AceleracaoXBola.insert(o, pontosAbolaX)
for n in range(0, len(VelocidadeXBola)):
  AceleracaoYBola.insert(n, pontosAbolaY)

CopiaAceleracaoXBola = AceleracaoXBola.copy()
CopiaAceleracaoYBola = AceleracaoYBola.copy()
  
PosInicialRoboX = float(input("Digite a posição inicial do robo em x: "))
PosInicialRoboY = float(input("Digite a posição inicial do robo em y: "))
print("A posição inicial do robo em X e em Y é: (%.2f, %.2f)" %(PosInicialRoboX, PosInicialRoboY))
distanciaT = [] #array de todos os valores de distancia entre dois pontos
velocidadeR = 2.8 #velociade maxima definida a partir dos dados obtidos no artigo
velBolaX = [0]
velBolaY = [0]
raio = 0.0705 #em metros
print("O raio de interceptação é: %.4f metros" %raio)

def graficoTrajetoriaBola():
  matplotlib.pyplot.title('trajetória da bola e do robô')
  matplotlib.pyplot.xlabel('Posição em x (m)')
  matplotlib.pyplot.ylabel('Posição em y (m)')
  matplotlib.pyplot.plot(CopiaPosicaoXBola, CopiaPosicaoYBola,'g', PosRoboX, PosRoboY,'mo--')
  matplotlib.pyplot.show() #exibir o grafico  
def graficoPosicaoxTempo():
  matplotlib.pyplot.title('Posicao em X(m) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Posição em x (m)')
  matplotlib.pyplot.plot( CopiaTempo,CopiaPosicaoXBola, 'g', tempoRobo, PosRoboX, 'mo--')
  matplotlib.pyplot.show() #exibir o grafico
  
def graficoPosicaoyTempo():
  matplotlib.pyplot.title('Posicao em Y(m) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Posição em Y (m)')
  matplotlib.pyplot.plot( CopiaTempo,CopiaPosicaoYBola, 'g', tempoRobo, PosRoboY, 'mo--')
  matplotlib.pyplot.show() #exibir o grafico

def graficoVelocidadeXTempo():
  matplotlib.pyplot.title('Velocidade em X(m/s) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Velocidade em X (m/s)')
  matplotlib.pyplot.plot(CopiaTempo,CopiaVelocidadeXBola, 'g', tempoRobo, velocidadeX, 'mo--')
  matplotlib.pyplot.show()
  
def graficoVelocidadeYTempo():
  matplotlib.pyplot.title('Velocidade em Y(m/s) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Velocidade em Y (m/s)')
  matplotlib.pyplot.plot(CopiaTempo,CopiaVelocidadeYBola, 'g', tempoRobo, velocidadeY, 'mo--')
  matplotlib.pyplot.show() #exibir o grafico

def graficoAceleracaoXTempo():
  matplotlib.pyplot.title('Aceleração em X(m/s) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Aceleracao em X (m/s)')
  matplotlib.pyplot.plot(CopiaTempo, CopiaAceleracaoXBola, 'g', tempoRobo, aceleracaoRobo, 'mo--')
  matplotlib.pyplot.show() #exibir o grafico
  
def graficoAceleracaoYTempo():
  matplotlib.pyplot.title('Aceleração em X(m/s) em função do tempo(s)')
  matplotlib.pyplot.xlabel('Tempo (s)')
  matplotlib.pyplot.ylabel('Aceleracao em X (m/s)')
  matplotlib.pyplot.plot(CopiaTempo, CopiaAceleracaoYBola, 'g', tempoRobo, aceleracaoRobo, 'mo--')
  matplotlib.pyplot.show() #exibir o grafico

def menuGrafico():
    print()
    print("Deseja visualizar algum gráfico? (Aperte o X para fechar o gráfico e visualizar outro)")
    print()
    print("Escolha uma das opções a seguir (digite 0 para sair):")
    print()
    print("1 - Gráfico das trajetórias do robô e da bola até o ponto de interceptação")
    print("2 - Gráfico das coordenadas do robô e da bola em X até o ponto de interceptação em função do tempo")
    print("3 - Gráfico das coordenadas do robô e da bola em Y até o ponto de interceptação em função do tempo")
    print("4 - Gráfico do componente Vx do robô e da bola até o ponto de interceptação em função do tempo")
    print("5 - Gráfico do componente Vy do robô e da bola até o ponto de interceptação em função do tempo")
    print("6 - Gráfico do componente Ax do robô e da bola até o ponto de interceptação em função do tempo")
    print("7 - Gráfico do componente Ay do robô e da bola até o ponto de interceptação em função do tempo")
    print("8 - Gráfico da distância relativa d em X entre robô e bola até o ponto de interceptação em função do tempo")
    option = int(input("Digite a opção escolhida: "))
   

    if option == 1:
      graficoTrajetoriaBola()
      menuGrafico() 
    elif option == 2:
      graficoPosicaoxTempo()
      menuGrafico() 
    elif option == 3:
      graficoPosicaoyTempo()
      menuGrafico()      
    elif option == 4:
      graficoVelocidadeXTempo()
      menuGrafico()
    elif option == 5:
      graficoVelocidadeYTempo()
      menuGrafico()     
    elif option == 6:
      graficoAceleracaoXTempo()
      menuGrafico()   
    elif option == 7:
      graficoAceleracaoYTempo()
      menuGrafico()    
    elif option == 8:
      graficoAceleracaoYTempo()
      menuGrafico()  
    elif option == 0:
      print("Você chegou ao final do programa! :)")
      print("Reinicie o programa para testar outras coordenadas.")
      pass #para encerrar o programa 
    else:
      print("Opção inválida! Tente novamente.")
      menuGrafico()  
    
    
      
def DistanciaDoisPontos(X1, Y1, X2, Y2):
  distancia = sqrt(((X2 - X1)**2) + ((Y2 - Y1)**2))
  return distancia

def main(): #chamar todas as funções de fora; inclusive dos gráficos 
  for i in range(0, 306): 
    distancia = DistanciaDoisPontos(PosInicialRoboX, PosInicialRoboY, PosicaoXBola[i], PosicaoYBola[i])
    distanciaT.insert(i,(distancia))

  tempoEspera = -1
  
  while tempoEspera < 0:
  
    MenorValor = min(distanciaT)
    IndexMenorValor = distanciaT.index(MenorValor)

    maisProximoX = PosicaoXBola[IndexMenorValor]
    maisProximoY = PosicaoYBola[IndexMenorValor]
      
    #deslocamento do robo
    deslocamentox = (maisProximoX - PosInicialRoboX) #cateto
    deslocamentoy = (maisProximoY - PosInicialRoboY) #cateto 
    
    deslocamentoT = sqrt((deslocamentox**2) + (deslocamentoy**2)) #modulo do deslocamento
    
    tempoDeslocamentoRobo = deslocamentoT/velocidadeR #2.8; usando a formula de v = d/t e isolando o t (t = d/v)
    tempoDeslocamentoBola = tempo[IndexMenorValor]
    tempoEspera = tempoDeslocamentoBola - tempoDeslocamentoRobo

    if tempoEspera < 0:
      distanciaT.pop(IndexMenorValor)
      tempo.pop(IndexMenorValor)
      PosicaoXBola.pop(IndexMenorValor)
      PosicaoYBola.pop(IndexMenorValor)
      VelocidadeYBola.pop(IndexMenorValor)
      VelocidadeXBola.pop(IndexMenorValor)
      AceleracaoXBola.pop(IndexMenorValor)
      AceleracaoYBola.pop(IndexMenorValor)

  distanciaX = maisProximoX - PosInicialRoboX #distancia entre o robô e o potno mais proximo em x
  distanciaY = maisProximoY - PosInicialRoboY #distancia entre o robô e o potno mais proximo em y

  incrementoX = distanciaX/10 #calcular a distancia percorrida no eixo x durante 10 pontos
  incrementoY = distanciaY/10 #calcular a distancia percorrida no eixo y durante 10 pontos

  global PosRoboX
  global PosRoboY
  PosRoboX = []
  PosRoboY = []
  pontoRoboX = PosInicialRoboX
  pontoRoboY = PosInicialRoboY
  
  print("Distância andada em cada ponto de x: %.2fm" %incrementoX)
  print("Distância andada em cada ponto de y: %.2fm" % incrementoY)

  
  print()
  print('Trajetória:')
  print()
  
  for r in range(0, 10):
    pontoRoboX = pontoRoboX + incrementoX 
    PosRoboX.insert(r,(pontoRoboX))
    pontoRoboY = pontoRoboY + incrementoY
    PosRoboY.insert(r,(pontoRoboY))

    print("%.2f, %.2f" %(PosRoboX[r], PosRoboY[r]))
  print()
  print("*****A bola foi interceptada pelo robô!*****")
  print("A distância entre a bola e robô é menor que o raio de interceptação.")
  print()
  
  IncrementoTempo = tempoDeslocamentoRobo/10
  global tempoRobo
  tempoRobo = []
  pontoTempo = 0
  print("Tempo: ")
  print()
  for t in range(0, 10):
    pontoTempo = pontoTempo + IncrementoTempo
    tempoRobo.insert(t, pontoTempo)

    print("%.2f s" % (tempoRobo[t]))
  print()

  anguloTeta = atan(deslocamentoy/deslocamentox) #usado para achar o angulo da direção em que o robo vai andar
  velocidadeYponto = velocidadeR*sin(anguloTeta) #decompondo a velocidade no eixo x
  velocidadeXponto = velocidadeR*cos(anguloTeta) #decompondo a velocidade no eixo y
  
  global velocidadeX
  global velocidadeY
  velocidadeY = []
  velocidadeX = []
  
  for j in range(0, 10):
    velocidadeY.insert(j, velocidadeYponto)
    velocidadeX.insert(j, velocidadeXponto)
  aceleracaoPonto = 0
  global aceleracaoRobo
  aceleracaoRobo = []
  for u in range(0, 10):
    aceleracaoRobo.insert(u, aceleracaoPonto) 

  choice = input('Deseja visualizar mais informações cinemáticas relevantes?(S/N): ')
  if choice == 'S':
    print("O deslocamento total é de: %.2f metros" %(deslocamentoT))
    print("O tempo de interceptação é de : %.2f segundos" %tempoDeslocamentoRobo)
    print("Deslocamento em x : %.2f metros" %deslocamentox)
    print("Deslocamento em y : %.2f metros" %deslocamentoy)
    print("A coordenada mais próxima é: (%.2f, %.2f)" % (maisProximoX, maisProximoY))
    print("O index do menor valor é %d" % IndexMenorValor)
    print("A menor distância é: %.2f metros" % MenorValor)
    print("O tempo de espera do robô será de: %.2f segundos" % (tempoEspera))
    print("Velocidade em Y: %.2f m/s" %velocidadeY[0])
    print("Velocidade em X: %.2f m/s" % velocidadeX[0]) 
    print("Aceleração do robô: %.2f" % aceleracaoRobo[u])  
    menuGrafico()
  elif choice == 'N':
    menuGrafico()
  
  
distanciaTesteRaio = DistanciaDoisPontos(PosInicialRoboX, PosInicialRoboY, PosicaoXBola[0], PosicaoYBola[0])
if PosInicialRoboX <=9 and PosInicialRoboY <=6:
  if distanciaTesteRaio > raio: #if usando o raio de interceptação da bola
    main()
    menuGrafico()
  else:
    print("O robô já está ao lado da bola!")
    menuGrafico()
else:
    print("O robô está fora do campo.")