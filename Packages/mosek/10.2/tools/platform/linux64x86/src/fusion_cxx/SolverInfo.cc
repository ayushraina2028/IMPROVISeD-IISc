#include <SolverInfo.h>
namespace mosek {
namespace fusion {
  std::vector<std::string> SolverInfo::dinfnames  {
    "anaProScalarizedConstraintMatrixDensity",
    "biCleanDualTime",
    "biCleanPrimalTime",
    "biCleanTime",
    "biDualTime",
    "biPrimalTime",
    "biTime",
    "intpntDualFeas",
    "intpntDualObj",
    "intpntFactorNumFlops",
    "intpntOptStatus",
    "intpntOrderTime",
    "intpntPrimalFeas",
    "intpntPrimalObj",
    "intpntTime",
    "mioCliqueSelectionTime",
    "mioCliqueSeparationTime",
    "mioCmirSelectionTime",
    "mioCmirSeparationTime",
    "mioConstructSolutionObj",
    "mioDualBoundAfterPresolve",
    "mioGmiSelectionTime",
    "mioGmiSeparationTime",
    "mioImpliedBoundSelectionTime",
    "mioImpliedBoundSeparationTime",
    "mioInitialFeasibleSolutionObj",
    "mioKnapsackCoverSelectionTime",
    "mioKnapsackCoverSeparationTime",
    "mioLiproSelectionTime",
    "mioLiproSeparationTime",
    "mioObjAbsGap",
    "mioObjBound",
    "mioObjInt",
    "mioObjRelGap",
    "mioProbingTime",
    "mioRootCutSelectionTime",
    "mioRootCutSeparationTime",
    "mioRootOptimizerTime",
    "mioRootPresolveTime",
    "mioRootTime",
    "mioSymmetryDetectionTime",
    "mioSymmetryFactor",
    "mioTime",
    "mioUserObjCut",
    "optimizerTicks",
    "optimizerTime",
    "presolveEliTime",
    "presolveLindepTime",
    "presolveTime",
    "presolveTotalPrimalPerturbation",
    "primalRepairPenaltyObj",
    "qcqoReformulateMaxPerturbation",
    "qcqoReformulateTime",
    "qcqoReformulateWorstCholeskyColumnScaling",
    "qcqoReformulateWorstCholeskyDiagScaling",
    "readDataTime",
    "remoteTime",
    "simDualTime",
    "simFeas",
    "simObj",
    "simPrimalTime",
    "simTime",
    "solBasDualObj",
    "solBasDviolcon",
    "solBasDviolvar",
    "solBasNrmBarx",
    "solBasNrmSlc",
    "solBasNrmSlx",
    "solBasNrmSuc",
    "solBasNrmSux",
    "solBasNrmXc",
    "solBasNrmXx",
    "solBasNrmY",
    "solBasPrimalObj",
    "solBasPviolcon",
    "solBasPviolvar",
    "solItgNrmBarx",
    "solItgNrmXc",
    "solItgNrmXx",
    "solItgPrimalObj",
    "solItgPviolacc",
    "solItgPviolbarvar",
    "solItgPviolcon",
    "solItgPviolcones",
    "solItgPvioldjc",
    "solItgPviolitg",
    "solItgPviolvar",
    "solItrDualObj",
    "solItrDviolacc",
    "solItrDviolbarvar",
    "solItrDviolcon",
    "solItrDviolcones",
    "solItrDviolvar",
    "solItrNrmBars",
    "solItrNrmBarx",
    "solItrNrmSlc",
    "solItrNrmSlx",
    "solItrNrmSnx",
    "solItrNrmSuc",
    "solItrNrmSux",
    "solItrNrmXc",
    "solItrNrmXx",
    "solItrNrmY",
    "solItrPrimalObj",
    "solItrPviolacc",
    "solItrPviolbarvar",
    "solItrPviolcon",
    "solItrPviolcones",
    "solItrPviolvar",
    "toConicTime",
    "writeDataTime" };
  std::vector<std::string> SolverInfo::iinfnames  {
    "anaProNumCon",
    "anaProNumConEq",
    "anaProNumConFr",
    "anaProNumConLo",
    "anaProNumConRa",
    "anaProNumConUp",
    "anaProNumVar",
    "anaProNumVarBin",
    "anaProNumVarCont",
    "anaProNumVarEq",
    "anaProNumVarFr",
    "anaProNumVarInt",
    "anaProNumVarLo",
    "anaProNumVarRa",
    "anaProNumVarUp",
    "intpntFactorDimDense",
    "intpntIter",
    "intpntNumThreads",
    "intpntSolveDual",
    "mioAbsgapSatisfied",
    "mioCliqueTableSize",
    "mioConstructSolution",
    "mioInitialFeasibleSolution",
    "mioNodeDepth",
    "mioNumActiveNodes",
    "mioNumActiveRootCuts",
    "mioNumBranch",
    "mioNumIntSolutions",
    "mioNumRelax",
    "mioNumRepeatedPresolve",
    "mioNumRestarts",
    "mioNumRootCutRounds",
    "mioNumSelectedCliqueCuts",
    "mioNumSelectedCmirCuts",
    "mioNumSelectedGomoryCuts",
    "mioNumSelectedImpliedBoundCuts",
    "mioNumSelectedKnapsackCoverCuts",
    "mioNumSelectedLiproCuts",
    "mioNumSeparatedCliqueCuts",
    "mioNumSeparatedCmirCuts",
    "mioNumSeparatedGomoryCuts",
    "mioNumSeparatedImpliedBoundCuts",
    "mioNumSeparatedKnapsackCoverCuts",
    "mioNumSeparatedLiproCuts",
    "mioNumSolvedNodes",
    "mioNumbin",
    "mioNumbinconevar",
    "mioNumcon",
    "mioNumcone",
    "mioNumconevar",
    "mioNumcont",
    "mioNumcontconevar",
    "mioNumdexpcones",
    "mioNumdjc",
    "mioNumdpowcones",
    "mioNumint",
    "mioNumintconevar",
    "mioNumpexpcones",
    "mioNumppowcones",
    "mioNumqcones",
    "mioNumrqcones",
    "mioNumvar",
    "mioObjBoundDefined",
    "mioPresolvedNumbin",
    "mioPresolvedNumbinconevar",
    "mioPresolvedNumcon",
    "mioPresolvedNumcone",
    "mioPresolvedNumconevar",
    "mioPresolvedNumcont",
    "mioPresolvedNumcontconevar",
    "mioPresolvedNumdexpcones",
    "mioPresolvedNumdjc",
    "mioPresolvedNumdpowcones",
    "mioPresolvedNumint",
    "mioPresolvedNumintconevar",
    "mioPresolvedNumpexpcones",
    "mioPresolvedNumppowcones",
    "mioPresolvedNumqcones",
    "mioPresolvedNumrqcones",
    "mioPresolvedNumvar",
    "mioRelgapSatisfied",
    "mioTotalNumSelectedCuts",
    "mioTotalNumSeparatedCuts",
    "mioUserObjCut",
    "optNumcon",
    "optNumvar",
    "optimizeResponse",
    "presolveNumPrimalPerturbations",
    "purifyDualSuccess",
    "purifyPrimalSuccess",
    "rdNumbarvar",
    "rdNumcon",
    "rdNumcone",
    "rdNumintvar",
    "rdNumq",
    "rdNumvar",
    "rdProtype",
    "simDualDegIter",
    "simDualHotstart",
    "simDualHotstartLu",
    "simDualInfIter",
    "simDualIter",
    "simNumcon",
    "simNumvar",
    "simPrimalDegIter",
    "simPrimalHotstart",
    "simPrimalHotstartLu",
    "simPrimalInfIter",
    "simPrimalIter",
    "simSolveDual",
    "solBasProsta",
    "solBasSolsta",
    "solItgProsta",
    "solItgSolsta",
    "solItrProsta",
    "solItrSolsta",
    "stoNumARealloc" };
  std::vector<std::string> SolverInfo::liinfnames {
    "anaProScalarizedConstraintMatrixNumColumns",
    "anaProScalarizedConstraintMatrixNumNz",
    "anaProScalarizedConstraintMatrixNumRows",
    "biCleanDualDegIter",
    "biCleanDualIter",
    "biCleanPrimalDegIter",
    "biCleanPrimalIter",
    "biDualIter",
    "biPrimalIter",
    "intpntFactorNumNz",
    "mioAnz",
    "mioIntpntIter",
    "mioNumDualIllposedCer",
    "mioNumPrimIllposedCer",
    "mioPresolvedAnz",
    "mioSimplexIter",
    "rdNumacc",
    "rdNumanz",
    "rdNumdjc",
    "rdNumqnz",
    "simplexIter" };
  MSKdinfiteme  SolverInfo::dinfsyms[]  = { MSK_DINF_ANA_PRO_SCALARIZED_CONSTRAINT_MATRIX_DENSITY,MSK_DINF_BI_CLEAN_DUAL_TIME,MSK_DINF_BI_CLEAN_PRIMAL_TIME,MSK_DINF_BI_CLEAN_TIME,MSK_DINF_BI_DUAL_TIME,MSK_DINF_BI_PRIMAL_TIME,MSK_DINF_BI_TIME,MSK_DINF_INTPNT_DUAL_FEAS,MSK_DINF_INTPNT_DUAL_OBJ,MSK_DINF_INTPNT_FACTOR_NUM_FLOPS,MSK_DINF_INTPNT_OPT_STATUS,MSK_DINF_INTPNT_ORDER_TIME,MSK_DINF_INTPNT_PRIMAL_FEAS,MSK_DINF_INTPNT_PRIMAL_OBJ,MSK_DINF_INTPNT_TIME,MSK_DINF_MIO_CLIQUE_SELECTION_TIME,MSK_DINF_MIO_CLIQUE_SEPARATION_TIME,MSK_DINF_MIO_CMIR_SELECTION_TIME,MSK_DINF_MIO_CMIR_SEPARATION_TIME,MSK_DINF_MIO_CONSTRUCT_SOLUTION_OBJ,MSK_DINF_MIO_DUAL_BOUND_AFTER_PRESOLVE,MSK_DINF_MIO_GMI_SELECTION_TIME,MSK_DINF_MIO_GMI_SEPARATION_TIME,MSK_DINF_MIO_IMPLIED_BOUND_SELECTION_TIME,MSK_DINF_MIO_IMPLIED_BOUND_SEPARATION_TIME,MSK_DINF_MIO_INITIAL_FEASIBLE_SOLUTION_OBJ,MSK_DINF_MIO_KNAPSACK_COVER_SELECTION_TIME,MSK_DINF_MIO_KNAPSACK_COVER_SEPARATION_TIME,MSK_DINF_MIO_LIPRO_SELECTION_TIME,MSK_DINF_MIO_LIPRO_SEPARATION_TIME,MSK_DINF_MIO_OBJ_ABS_GAP,MSK_DINF_MIO_OBJ_BOUND,MSK_DINF_MIO_OBJ_INT,MSK_DINF_MIO_OBJ_REL_GAP,MSK_DINF_MIO_PROBING_TIME,MSK_DINF_MIO_ROOT_CUT_SELECTION_TIME,MSK_DINF_MIO_ROOT_CUT_SEPARATION_TIME,MSK_DINF_MIO_ROOT_OPTIMIZER_TIME,MSK_DINF_MIO_ROOT_PRESOLVE_TIME,MSK_DINF_MIO_ROOT_TIME,MSK_DINF_MIO_SYMMETRY_DETECTION_TIME,MSK_DINF_MIO_SYMMETRY_FACTOR,MSK_DINF_MIO_TIME,MSK_DINF_MIO_USER_OBJ_CUT,MSK_DINF_OPTIMIZER_TICKS,MSK_DINF_OPTIMIZER_TIME,MSK_DINF_PRESOLVE_ELI_TIME,MSK_DINF_PRESOLVE_LINDEP_TIME,MSK_DINF_PRESOLVE_TIME,MSK_DINF_PRESOLVE_TOTAL_PRIMAL_PERTURBATION,MSK_DINF_PRIMAL_REPAIR_PENALTY_OBJ,MSK_DINF_QCQO_REFORMULATE_MAX_PERTURBATION,MSK_DINF_QCQO_REFORMULATE_TIME,MSK_DINF_QCQO_REFORMULATE_WORST_CHOLESKY_COLUMN_SCALING,MSK_DINF_QCQO_REFORMULATE_WORST_CHOLESKY_DIAG_SCALING,MSK_DINF_READ_DATA_TIME,MSK_DINF_REMOTE_TIME,MSK_DINF_SIM_DUAL_TIME,MSK_DINF_SIM_FEAS,MSK_DINF_SIM_OBJ,MSK_DINF_SIM_PRIMAL_TIME,MSK_DINF_SIM_TIME,MSK_DINF_SOL_BAS_DUAL_OBJ,MSK_DINF_SOL_BAS_DVIOLCON,MSK_DINF_SOL_BAS_DVIOLVAR,MSK_DINF_SOL_BAS_NRM_BARX,MSK_DINF_SOL_BAS_NRM_SLC,MSK_DINF_SOL_BAS_NRM_SLX,MSK_DINF_SOL_BAS_NRM_SUC,MSK_DINF_SOL_BAS_NRM_SUX,MSK_DINF_SOL_BAS_NRM_XC,MSK_DINF_SOL_BAS_NRM_XX,MSK_DINF_SOL_BAS_NRM_Y,MSK_DINF_SOL_BAS_PRIMAL_OBJ,MSK_DINF_SOL_BAS_PVIOLCON,MSK_DINF_SOL_BAS_PVIOLVAR,MSK_DINF_SOL_ITG_NRM_BARX,MSK_DINF_SOL_ITG_NRM_XC,MSK_DINF_SOL_ITG_NRM_XX,MSK_DINF_SOL_ITG_PRIMAL_OBJ,MSK_DINF_SOL_ITG_PVIOLACC,MSK_DINF_SOL_ITG_PVIOLBARVAR,MSK_DINF_SOL_ITG_PVIOLCON,MSK_DINF_SOL_ITG_PVIOLCONES,MSK_DINF_SOL_ITG_PVIOLDJC,MSK_DINF_SOL_ITG_PVIOLITG,MSK_DINF_SOL_ITG_PVIOLVAR,MSK_DINF_SOL_ITR_DUAL_OBJ,MSK_DINF_SOL_ITR_DVIOLACC,MSK_DINF_SOL_ITR_DVIOLBARVAR,MSK_DINF_SOL_ITR_DVIOLCON,MSK_DINF_SOL_ITR_DVIOLCONES,MSK_DINF_SOL_ITR_DVIOLVAR,MSK_DINF_SOL_ITR_NRM_BARS,MSK_DINF_SOL_ITR_NRM_BARX,MSK_DINF_SOL_ITR_NRM_SLC,MSK_DINF_SOL_ITR_NRM_SLX,MSK_DINF_SOL_ITR_NRM_SNX,MSK_DINF_SOL_ITR_NRM_SUC,MSK_DINF_SOL_ITR_NRM_SUX,MSK_DINF_SOL_ITR_NRM_XC,MSK_DINF_SOL_ITR_NRM_XX,MSK_DINF_SOL_ITR_NRM_Y,MSK_DINF_SOL_ITR_PRIMAL_OBJ,MSK_DINF_SOL_ITR_PVIOLACC,MSK_DINF_SOL_ITR_PVIOLBARVAR,MSK_DINF_SOL_ITR_PVIOLCON,MSK_DINF_SOL_ITR_PVIOLCONES,MSK_DINF_SOL_ITR_PVIOLVAR,MSK_DINF_TO_CONIC_TIME,MSK_DINF_WRITE_DATA_TIME };
  MSKiinfiteme  SolverInfo::iinfsyms[]  = { MSK_IINF_ANA_PRO_NUM_CON,MSK_IINF_ANA_PRO_NUM_CON_EQ,MSK_IINF_ANA_PRO_NUM_CON_FR,MSK_IINF_ANA_PRO_NUM_CON_LO,MSK_IINF_ANA_PRO_NUM_CON_RA,MSK_IINF_ANA_PRO_NUM_CON_UP,MSK_IINF_ANA_PRO_NUM_VAR,MSK_IINF_ANA_PRO_NUM_VAR_BIN,MSK_IINF_ANA_PRO_NUM_VAR_CONT,MSK_IINF_ANA_PRO_NUM_VAR_EQ,MSK_IINF_ANA_PRO_NUM_VAR_FR,MSK_IINF_ANA_PRO_NUM_VAR_INT,MSK_IINF_ANA_PRO_NUM_VAR_LO,MSK_IINF_ANA_PRO_NUM_VAR_RA,MSK_IINF_ANA_PRO_NUM_VAR_UP,MSK_IINF_INTPNT_FACTOR_DIM_DENSE,MSK_IINF_INTPNT_ITER,MSK_IINF_INTPNT_NUM_THREADS,MSK_IINF_INTPNT_SOLVE_DUAL,MSK_IINF_MIO_ABSGAP_SATISFIED,MSK_IINF_MIO_CLIQUE_TABLE_SIZE,MSK_IINF_MIO_CONSTRUCT_SOLUTION,MSK_IINF_MIO_INITIAL_FEASIBLE_SOLUTION,MSK_IINF_MIO_NODE_DEPTH,MSK_IINF_MIO_NUM_ACTIVE_NODES,MSK_IINF_MIO_NUM_ACTIVE_ROOT_CUTS,MSK_IINF_MIO_NUM_BRANCH,MSK_IINF_MIO_NUM_INT_SOLUTIONS,MSK_IINF_MIO_NUM_RELAX,MSK_IINF_MIO_NUM_REPEATED_PRESOLVE,MSK_IINF_MIO_NUM_RESTARTS,MSK_IINF_MIO_NUM_ROOT_CUT_ROUNDS,MSK_IINF_MIO_NUM_SELECTED_CLIQUE_CUTS,MSK_IINF_MIO_NUM_SELECTED_CMIR_CUTS,MSK_IINF_MIO_NUM_SELECTED_GOMORY_CUTS,MSK_IINF_MIO_NUM_SELECTED_IMPLIED_BOUND_CUTS,MSK_IINF_MIO_NUM_SELECTED_KNAPSACK_COVER_CUTS,MSK_IINF_MIO_NUM_SELECTED_LIPRO_CUTS,MSK_IINF_MIO_NUM_SEPARATED_CLIQUE_CUTS,MSK_IINF_MIO_NUM_SEPARATED_CMIR_CUTS,MSK_IINF_MIO_NUM_SEPARATED_GOMORY_CUTS,MSK_IINF_MIO_NUM_SEPARATED_IMPLIED_BOUND_CUTS,MSK_IINF_MIO_NUM_SEPARATED_KNAPSACK_COVER_CUTS,MSK_IINF_MIO_NUM_SEPARATED_LIPRO_CUTS,MSK_IINF_MIO_NUM_SOLVED_NODES,MSK_IINF_MIO_NUMBIN,MSK_IINF_MIO_NUMBINCONEVAR,MSK_IINF_MIO_NUMCON,MSK_IINF_MIO_NUMCONE,MSK_IINF_MIO_NUMCONEVAR,MSK_IINF_MIO_NUMCONT,MSK_IINF_MIO_NUMCONTCONEVAR,MSK_IINF_MIO_NUMDEXPCONES,MSK_IINF_MIO_NUMDJC,MSK_IINF_MIO_NUMDPOWCONES,MSK_IINF_MIO_NUMINT,MSK_IINF_MIO_NUMINTCONEVAR,MSK_IINF_MIO_NUMPEXPCONES,MSK_IINF_MIO_NUMPPOWCONES,MSK_IINF_MIO_NUMQCONES,MSK_IINF_MIO_NUMRQCONES,MSK_IINF_MIO_NUMVAR,MSK_IINF_MIO_OBJ_BOUND_DEFINED,MSK_IINF_MIO_PRESOLVED_NUMBIN,MSK_IINF_MIO_PRESOLVED_NUMBINCONEVAR,MSK_IINF_MIO_PRESOLVED_NUMCON,MSK_IINF_MIO_PRESOLVED_NUMCONE,MSK_IINF_MIO_PRESOLVED_NUMCONEVAR,MSK_IINF_MIO_PRESOLVED_NUMCONT,MSK_IINF_MIO_PRESOLVED_NUMCONTCONEVAR,MSK_IINF_MIO_PRESOLVED_NUMDEXPCONES,MSK_IINF_MIO_PRESOLVED_NUMDJC,MSK_IINF_MIO_PRESOLVED_NUMDPOWCONES,MSK_IINF_MIO_PRESOLVED_NUMINT,MSK_IINF_MIO_PRESOLVED_NUMINTCONEVAR,MSK_IINF_MIO_PRESOLVED_NUMPEXPCONES,MSK_IINF_MIO_PRESOLVED_NUMPPOWCONES,MSK_IINF_MIO_PRESOLVED_NUMQCONES,MSK_IINF_MIO_PRESOLVED_NUMRQCONES,MSK_IINF_MIO_PRESOLVED_NUMVAR,MSK_IINF_MIO_RELGAP_SATISFIED,MSK_IINF_MIO_TOTAL_NUM_SELECTED_CUTS,MSK_IINF_MIO_TOTAL_NUM_SEPARATED_CUTS,MSK_IINF_MIO_USER_OBJ_CUT,MSK_IINF_OPT_NUMCON,MSK_IINF_OPT_NUMVAR,MSK_IINF_OPTIMIZE_RESPONSE,MSK_IINF_PRESOLVE_NUM_PRIMAL_PERTURBATIONS,MSK_IINF_PURIFY_DUAL_SUCCESS,MSK_IINF_PURIFY_PRIMAL_SUCCESS,MSK_IINF_RD_NUMBARVAR,MSK_IINF_RD_NUMCON,MSK_IINF_RD_NUMCONE,MSK_IINF_RD_NUMINTVAR,MSK_IINF_RD_NUMQ,MSK_IINF_RD_NUMVAR,MSK_IINF_RD_PROTYPE,MSK_IINF_SIM_DUAL_DEG_ITER,MSK_IINF_SIM_DUAL_HOTSTART,MSK_IINF_SIM_DUAL_HOTSTART_LU,MSK_IINF_SIM_DUAL_INF_ITER,MSK_IINF_SIM_DUAL_ITER,MSK_IINF_SIM_NUMCON,MSK_IINF_SIM_NUMVAR,MSK_IINF_SIM_PRIMAL_DEG_ITER,MSK_IINF_SIM_PRIMAL_HOTSTART,MSK_IINF_SIM_PRIMAL_HOTSTART_LU,MSK_IINF_SIM_PRIMAL_INF_ITER,MSK_IINF_SIM_PRIMAL_ITER,MSK_IINF_SIM_SOLVE_DUAL,MSK_IINF_SOL_BAS_PROSTA,MSK_IINF_SOL_BAS_SOLSTA,MSK_IINF_SOL_ITG_PROSTA,MSK_IINF_SOL_ITG_SOLSTA,MSK_IINF_SOL_ITR_PROSTA,MSK_IINF_SOL_ITR_SOLSTA,MSK_IINF_STO_NUM_A_REALLOC };
  MSKliinfiteme SolverInfo::liinfsyms[] = { MSK_LIINF_ANA_PRO_SCALARIZED_CONSTRAINT_MATRIX_NUM_COLUMNS,MSK_LIINF_ANA_PRO_SCALARIZED_CONSTRAINT_MATRIX_NUM_NZ,MSK_LIINF_ANA_PRO_SCALARIZED_CONSTRAINT_MATRIX_NUM_ROWS,MSK_LIINF_BI_CLEAN_DUAL_DEG_ITER,MSK_LIINF_BI_CLEAN_DUAL_ITER,MSK_LIINF_BI_CLEAN_PRIMAL_DEG_ITER,MSK_LIINF_BI_CLEAN_PRIMAL_ITER,MSK_LIINF_BI_DUAL_ITER,MSK_LIINF_BI_PRIMAL_ITER,MSK_LIINF_INTPNT_FACTOR_NUM_NZ,MSK_LIINF_MIO_ANZ,MSK_LIINF_MIO_INTPNT_ITER,MSK_LIINF_MIO_NUM_DUAL_ILLPOSED_CER,MSK_LIINF_MIO_NUM_PRIM_ILLPOSED_CER,MSK_LIINF_MIO_PRESOLVED_ANZ,MSK_LIINF_MIO_SIMPLEX_ITER,MSK_LIINF_RD_NUMACC,MSK_LIINF_RD_NUMANZ,MSK_LIINF_RD_NUMDJC,MSK_LIINF_RD_NUMQNZ,MSK_LIINF_SIMPLEX_ITER };
  bool SolverInfo::getdouinf(const std::string & infname, MSKdinfiteme & key )
  {
    auto it = std::lower_bound(dinfnames.begin(),dinfnames.end(),infname);
    if (*it == infname)
    {
      key = dinfsyms[&(*it)-&(dinfnames.front())];
      return true;
    }
    else
    {
      return false;
    }
  }
  bool SolverInfo::getintinf(const std::string & infname, MSKiinfiteme & key )
  {
    auto it = std::lower_bound(iinfnames.begin(),iinfnames.end(),infname);
    if (*it == infname)
    {
      key = iinfsyms[&(*it)-&(iinfnames.front())];
      return true;
    }
    else
    {
      return false;
    }
  }
  bool SolverInfo::getlintinf(const std::string & infname, MSKliinfiteme & key )
  {
    auto it = std::lower_bound(liinfnames.begin(),liinfnames.end(),infname);
    if (*it == infname)
    {
      key = liinfsyms[&(*it)-&(liinfnames.front())];
      return true;
    }
    else
    {
      return false;
    }
  }
} /* namespace fusion */
} /* namespace mosek */
