from mc3s_pywrapper.utilities import string_util as su

def write_topmon(simObj,topmonFile="topmon.inp"):

  topmon = ""

  topmon += "&io\n"

  if simObj.io.file_input is not None:
    topmon += "  file_input= {}\n".format(simObj.io.file_input)
  if simObj.io.file_restart is not None:
    topmon += "  file_restart= {}\n".format(simObj.io.file_restart)
  if simObj.io.file_struct is not None:
    topmon += "  file_struct= {}\n".format(simObj.io.file_struct)
  if simObj.io.file_run is not None:
    topmon += "  file_run= {}\n".format(simObj.io.file_run)
  if simObj.io.file_movie is not None:
    topmon += "  file_movie= {}\n".format(simObj.io.file_movie)
  if simObj.io.file_solute is not None:
    topmon += "  file_solute= {}\n".format(simObj.io.file_solute)
  if simObj.io.file_traj is not None:
    topmon += "  file_traj= {}\n".format(simObj.io.file_traj)
  if simObj.io.io_output is not None:
    topmon += "  io_output= {}\n".format(simObj.io.io_output)
  if simObj.io.run_num is not None:
    topmon += "  run_num= {}\n".format(simObj.io.run_num)
  if simObj.io.suffix is not None:
    topmon += "  suffix= {}\n".format(simObj.io.suffix)
  if simObj.io.L_movie_xyz is not None:
    topmon += "  L_movie_xyz= {}\n".format(simObj.io.L_movie_xyz)
  if simObj.io.L_movie_pdb is not None:
    topmon += "  L_movie_pdb= {}\n".format(simObj.io.L_movie_pdb)
  if simObj.io.file_cbmc_bend is not None:
    topmon += "  file_cbmc_bend= {}\n".format(simObj.io.file_cbmc_bend)
  if simObj.io.ltraj is not None:
    topmon += "  ltraj= {}\n".format(su.logicToString(simObj.io.ltraj))

  topmon += "/ \n\n"

  topmon += "&system\n"

  if simObj.system.lnpt is not None:
    topmon += "  lnpt= {}\n".format(su.logicToString(simObj.system.lnpt))
  if simObj.system.lgibbs is not None:
    topmon += "  lgibbs= {}\n".format(su.logicToString(simObj.system.lgibbs))
  if simObj.system.lgrand is not None:
    topmon += "  lgrand= {}\n".format(su.logicToString(simObj.system.lgrand))
  if simObj.system.lvirial is not None:
    topmon += "  lvirial= {}\n".format(su.logicToString(simObj.system.lvirial))
  if simObj.system.lmipsw is not None:
    topmon += "  lmipsw= {}\n".format(su.logicToString(simObj.system.lmipsw))
  if simObj.system.lexpee is not None:
    topmon += "  lexpee= {}\n".format(su.logicToString(simObj.system.lexpee))
  if simObj.system.ldielect is not None:
    topmon += "  ldielect= {}\n".format(su.logicToString(simObj.system.ldielect))
  if simObj.system.lijall is not None:
    topmon += "  lijall= {}\n".format(su.logicToString(simObj.system.lijall))
  if simObj.system.lchgall is not None:
    topmon += "  lchgall= {}\n".format(su.logicToString(simObj.system.lchgall))
  if simObj.system.lewald is not None:
    topmon += "  lewald= {}\n".format(su.logicToString(simObj.system.lewald))
  if simObj.system.lrecip is not None:
    topmon += "  lrecip= {}\n".format(su.logicToString(simObj.system.lrecip))
  if simObj.system.lcutcm is not None:
    topmon += "  lcutcm= {}\n".format(su.logicToString(simObj.system.lcutcm))
  if simObj.system.ltailc is not None:
    topmon += "  ltailc= {}\n".format(su.logicToString(simObj.system.ltailc))
  if simObj.system.lshift is not None:
    topmon += "  lshift= {}\n".format(su.logicToString(simObj.system.lshift))
  if simObj.system.ldual is not None:
    topmon += "  ldual= {}\n".format(su.logicToString(simObj.system.ldual))
  if simObj.system.lneigh is not None:
    topmon += "  lneigh= {}\n".format(su.logicToString(simObj.system.lneigh))
  if simObj.system.L_Coul_CBMC is not None:
    topmon += "  L_Coul_CBMC= {}\n".format(su.logicToString(simObj.system.L_Coul_CBMC))
  if simObj.system.L_Ewald_Auto is not None:
    topmon += "  L_Ewald_Auto= {}\n".format(su.logicToString(simObj.system.L_Ewald_Auto))
  if simObj.system.lmixlb is not None:
    topmon += "  lmixlb= {}\n".format(su.logicToString(simObj.system.lmixlb))
  if simObj.system.lmixjo is not None:
    topmon += "  lmixjo= {}\n".format(su.logicToString(simObj.system.lmixjo))
  if simObj.system.lmixwh is not None:
    topmon += "  lmixwh= {}\n".format(su.logicToString(simObj.system.lmixwh))
  if simObj.system.lmixkong is not None:
    topmon += "  lmixkong= {}\n".format(su.logicToString(simObj.system.lmixkong))
  if simObj.system.losmoticnvt is not None:
    topmon += "  losmoticnvt= {}\n".format(su.logicToString(simObj.system.losmoticnvt))
  if simObj.system.lanes is not None:
    topmon += "  lanes= {}\n".format(su.logicToString(simObj.system.lanes))
  if simObj.system.lpbc is not None:
    topmon += "  lpbc= {}\n".format(su.logicToString(simObj.system.lpbc))
  if simObj.system.lpbcx is not None:
    topmon += "  lpbcx= {}\n".format(su.logicToString(simObj.system.lpbcx))
  if simObj.system.lpbcy is not None:
    topmon += "  lpbcy= {}\n".format(su.logicToString(simObj.system.lpbcy))
  if simObj.system.lpbcz is not None:
    topmon += "  lpbcz= {}\n".format(su.logicToString(simObj.system.lpbcz))
  if simObj.system.lfold is not None:
    topmon += "  lfold= {}\n".format(su.logicToString(simObj.system.lfold))
  if simObj.system.lexzeo is not None:
    topmon += "  lexzeo= {}\n".format(su.logicToString(simObj.system.lexzeo))
  if simObj.system.lslit is not None:
    topmon += "  lslit= {}\n".format(su.logicToString(simObj.system.lslit))
  if simObj.system.lgraphite is not None:
    topmon += "  lgraphite= {}\n".format(su.logicToString(simObj.system.lgraphite))
  if simObj.system.lsami is not None:
    topmon += "  lsami= {}\n".format(su.logicToString(simObj.system.lsami))
  if simObj.system.lmuir is not None:
    topmon += "  lmuir= {}\n".format(su.logicToString(simObj.system.lmuir))
  if simObj.system.lelect_field is not None:
    topmon += "  lelect_field= {}\n".format(su.logicToString(simObj.system.lelect_field))
  if simObj.system.lgaro is not None:
    topmon += "  lgaro= {}\n".format(su.logicToString(simObj.system.lgaro))
  if simObj.system.lionic is not None:
    topmon += "  lionic= {}\n".format(su.logicToString(simObj.system.lionic))
  if simObj.system.L_spline is not None:
    topmon += "  L_spline= {}\n".format(su.logicToString(simObj.system.L_spline))
  if simObj.system.L_linear is not None:
    topmon += "  L_linear= {}\n".format(su.logicToString(simObj.system.L_linear))
  if simObj.system.L_vib_table is not None:
    topmon += "  L_vib_table= {}\n".format(su.logicToString(simObj.system.L_vib_table))
  if simObj.system.L_bend_table is not None:
    topmon += "  L_bend_table= {}\n".format(su.logicToString(simObj.system.L_bend_table))
  if simObj.system.L_elect_table is not None:
    topmon += "  L_elect_table= {}\n".format(su.logicToString(simObj.system.L_elect_table))
  if simObj.system.L_cbmc_bend is not None:
    topmon += "  L_cbmc_bend= {}\n".format(su.logicToString(simObj.system.L_cbmc_bend))
  if simObj.system.lkdtree is not None:
    topmon += "  lkdtree= {}\n".format(su.logicToString(simObj.system.lkdtree))

  topmon += "/ \n\n\n"

  topmon += "ATOMS\n"

  if simObj.atoms is not None:
    for i in range(simObj.atoms.length):
      atm = simObj.atoms[i+1]
      topmon += "{} {} {} {} {} {}\n".format(atm.intID, atm.aType, atm.vdWParams.unrolledString(), atm.charge, atm.mass, atm.chemID, atm.chName)

  topmon += "END ATOMS\n\n\n"

  topmon += "NONBOND\n"
  # rest tbf
  topmon += "END NONBOND\n\n\n"

  topmon += "BONDS\n"

  if simObj.bonds is not None:
    for i in range(simObj.bonds.length):
      bond = simObj.bonds[i+1]
      topmon += "{} {} {} {}\n".format(bond.intID, bond.bType, bond.brvib, bond.brvibk.unrolledString())

  topmon += "END BONDS\n\n\n"


  topmon += "ANGLES\n"

  if simObj.angles is not None:
    for i in range(simObj.angles.length):
      angle = simObj.angles[i+1]
      topmon += "{} {} {} {}\n".format(angle.intID, angle.aType, angle.brben, angle.brbenk.unrolledString())

  topmon += "END ANGLES\n\n\n"

  topmon += "DIHEDRALS\n"

  if simObj.dihedrals is not None:
    for i in range(simObj.dihedrals.length):
      dih = simObj.dihedrals[i+1]
      topmon += "{} {} {}\n".format(dih.intID, dih.dType, dih.vtt.unrolledString())

  topmon += "END DIHEDRALS"

  with open(topmonFile,"w") as f:
    f.write(topmon)
