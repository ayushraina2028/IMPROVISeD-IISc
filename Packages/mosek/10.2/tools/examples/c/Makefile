
#
# Compile and run MOSEK examples
#

CC=gcc
IPATHS=-I../../platform/linux64x86/h
LPATHS=-L../../platform/linux64x86/bin -Wl,-rpath-link,../../platform/linux64x86/bin '-Wl,-rpath=$$ORIGIN/../../platform/linux64x86/bin'
LIBS=-lm

acc1: acc1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o acc1 acc1.c -lmosek64 $(LIBS)

acc2: acc2.c
	$(CC) -g $(IPATHS) $(LPATHS) -o acc2 acc2.c -lmosek64 $(LIBS)

blas_lapack: blas_lapack.c
	$(CC) -g $(IPATHS) $(LPATHS) -o blas_lapack blas_lapack.c -lmosek64 $(LIBS)

callback: callback.c
	$(CC) -g $(IPATHS) $(LPATHS) -o callback callback.c -lmosek64 $(LIBS)

portfolio_1_basic: portfolio_1_basic.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_1_basic portfolio_1_basic.c -lmosek64 $(LIBS)

portfolio_2_frontier: portfolio_2_frontier.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_2_frontier portfolio_2_frontier.c -lmosek64 $(LIBS)

portfolio_3_impact: portfolio_3_impact.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_3_impact portfolio_3_impact.c -lmosek64 $(LIBS)

portfolio_4_transcost: portfolio_4_transcost.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_4_transcost portfolio_4_transcost.c -lmosek64 $(LIBS)

portfolio_5_card: portfolio_5_card.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_5_card portfolio_5_card.c -lmosek64 $(LIBS)

portfolio_6_factor: portfolio_6_factor.c
	$(CC) -g $(IPATHS) $(LPATHS) -o portfolio_6_factor portfolio_6_factor.c -lmosek64 $(LIBS)

cqo1: cqo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o cqo1 cqo1.c -lmosek64 $(LIBS)

ceo1: ceo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o ceo1 ceo1.c -lmosek64 $(LIBS)

pow1: pow1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o pow1 pow1.c -lmosek64 $(LIBS)

djc1: djc1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o djc1 djc1.c -lmosek64 $(LIBS)

errorreporting: errorreporting.c
	$(CC) -g $(IPATHS) $(LPATHS) -o errorreporting errorreporting.c -lmosek64 $(LIBS)

feasrepairex1: feasrepairex1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o feasrepairex1 feasrepairex1.c -lmosek64 $(LIBS)

helloworld: helloworld.c
	$(CC) -g $(IPATHS) $(LPATHS) -o helloworld helloworld.c -lmosek64 $(LIBS)

lo1: lo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o lo1 lo1.c -lmosek64 $(LIBS)

lo2: lo2.c
	$(CC) -g $(IPATHS) $(LPATHS) -o lo2 lo2.c -lmosek64 $(LIBS)

logistic: logistic.c
	$(CC) -g $(IPATHS) $(LPATHS) -o logistic logistic.c -lmosek64 $(LIBS)

gp1: gp1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o gp1 gp1.c -lmosek64 $(LIBS)

milo1: milo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o milo1 milo1.c -lmosek64 $(LIBS)

mioinitsol: mioinitsol.c
	$(CC) -g $(IPATHS) $(LPATHS) -o mioinitsol mioinitsol.c -lmosek64 $(LIBS)

mico1: mico1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o mico1 mico1.c -lmosek64 $(LIBS)

opt_server_async: opt_server_async.c
	$(CC) -g $(IPATHS) $(LPATHS) -o opt_server_async opt_server_async.c -lmosek64 $(LIBS)

opt_server_sync: opt_server_sync.c
	$(CC) -g $(IPATHS) $(LPATHS) -o opt_server_sync opt_server_sync.c -lmosek64 $(LIBS)

parallel: parallel.c
	$(CC) -g $(IPATHS) $(LPATHS) -o parallel parallel.c -lmosek64 $(LIBS)

parameters: parameters.c
	$(CC) -g $(IPATHS) $(LPATHS) -o parameters parameters.c -lmosek64 $(LIBS)

pinfeas: pinfeas.c
	$(CC) -g $(IPATHS) $(LPATHS) -o pinfeas pinfeas.c -lmosek64 $(LIBS)

reoptimization: reoptimization.c
	$(CC) -g $(IPATHS) $(LPATHS) -o reoptimization reoptimization.c -lmosek64 $(LIBS)

qcqo1: qcqo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o qcqo1 qcqo1.c -lmosek64 $(LIBS)

qo1: qo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o qo1 qo1.c -lmosek64 $(LIBS)

response: response.c
	$(CC) -g $(IPATHS) $(LPATHS) -o response response.c -lmosek64 $(LIBS)

sdo1: sdo1.c
	$(CC) -g $(IPATHS) $(LPATHS) -o sdo1 sdo1.c -lmosek64 $(LIBS)

sdo2: sdo2.c
	$(CC) -g $(IPATHS) $(LPATHS) -o sdo2 sdo2.c -lmosek64 $(LIBS)

sdo_lmi: sdo_lmi.c
	$(CC) -g $(IPATHS) $(LPATHS) -o sdo_lmi sdo_lmi.c -lmosek64 $(LIBS)

sensitivity: sensitivity.c
	$(CC) -g $(IPATHS) $(LPATHS) -o sensitivity sensitivity.c -lmosek64 $(LIBS)

simple: simple.c
	$(CC) -g $(IPATHS) $(LPATHS) -o simple simple.c -lmosek64 $(LIBS)

solutionquality: solutionquality.c
	$(CC) -g $(IPATHS) $(LPATHS) -o solutionquality solutionquality.c -lmosek64 $(LIBS)

solvebasis: solvebasis.c
	$(CC) -g $(IPATHS) $(LPATHS) -o solvebasis solvebasis.c -lmosek64 $(LIBS)

solvelinear: solvelinear.c
	$(CC) -g $(IPATHS) $(LPATHS) -o solvelinear solvelinear.c -lmosek64 $(LIBS)

sparsecholesky: sparsecholesky.c
	$(CC) -g $(IPATHS) $(LPATHS) -o sparsecholesky sparsecholesky.c -lmosek64 $(LIBS)

unicode: unicode.c
	$(CC) -g $(IPATHS) $(LPATHS) -o unicode unicode.c -lmosek64 $(LIBS)

.PHONY: clean test all

all: acc1 acc2 blas_lapack callback portfolio_1_basic portfolio_2_frontier portfolio_3_impact portfolio_4_transcost portfolio_5_card portfolio_6_factor cqo1 ceo1 pow1 djc1 errorreporting feasrepairex1 helloworld lo1 lo2 logistic gp1 milo1 mioinitsol mico1 opt_server_async opt_server_sync parallel parameters pinfeas reoptimization qcqo1 qo1 response sdo1 sdo2 sdo_lmi sensitivity simple solutionquality solvebasis solvelinear sparsecholesky unicode

clean:
	rm -f acc1 acc2 blas_lapack callback portfolio_1_basic portfolio_2_frontier portfolio_3_impact portfolio_4_transcost portfolio_5_card portfolio_6_factor cqo1 ceo1 pow1 djc1 errorreporting feasrepairex1 helloworld lo1 lo2 logistic gp1 milo1 mioinitsol mico1 opt_server_async opt_server_sync parallel parameters pinfeas reoptimization qcqo1 qo1 response sdo1 sdo2 sdo_lmi sensitivity simple solutionquality solvebasis solvelinear sparsecholesky unicode

test: acc1 acc2 blas_lapack callback portfolio_1_basic portfolio_2_frontier portfolio_3_impact portfolio_4_transcost portfolio_5_card portfolio_6_factor cqo1 ceo1 pow1 djc1 errorreporting feasrepairex1 helloworld lo1 lo2 logistic gp1 milo1 mioinitsol mico1 opt_server_async opt_server_sync parallel parameters pinfeas reoptimization qcqo1 qo1 response sdo1 sdo2 sdo_lmi sensitivity simple solutionquality solvebasis solvelinear sparsecholesky unicode
	./acc1
	./acc2
	./blas_lapack
	./callback
	./portfolio_1_basic
	./portfolio_2_frontier
	./portfolio_3_impact
	./portfolio_4_transcost
	./portfolio_5_card
	./portfolio_6_factor
	./cqo1
	./ceo1
	./pow1
	./djc1
	./errorreporting
	./feasrepairex1
	./helloworld
	./lo1
	./lo2
	./logistic
	./gp1
	./milo1
	./mioinitsol
	./mico1
	./opt_server_async
	./opt_server_sync
	./parallel
	./parameters
	./pinfeas
	./reoptimization
	./qcqo1
	./qo1
	./response
	./sdo1
	./sdo2
	./sdo_lmi
	./sensitivity
	./simple
	./solutionquality
	./solvebasis
	./solvelinear
	./sparsecholesky
	./unicode
