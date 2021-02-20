from mc3s_pywrapper.utilities import string_util as su

def write_fort4(simObj,fort4File="fort.4"):

  fort4 = ""

  fort4 += "&mc_shared\n"

  if simObj.shared.seed is not None:
    fort4 += "  seed= {}\n".format(simObj.shared.seed)
  if simObj.shared.nbox is not None:
    fort4 += "  nbox= {}\n".format(simObj.shared.nbox)
  if simObj.shared.nmolty is not None:
    fort4 += "  nmolty= {}\n".format(simObj.shared.nmolty)
  if simObj.shared.nstep is not None:
    fort4 += "  nstep= {}\n".format(simObj.shared.nstep)
  if simObj.shared.lstop is not None:
    fort4 += "  lstop= {}\n".format(su.logicToString(simObj.shared.lstop))
  if simObj.shared.iratio is not None:
    fort4 += "  iratio= {}\n".format(simObj.shared.iratio)
  if simObj.shared.rmin is not None:
    fort4 += "  rmin= {}\n".format(simObj.shared.rmin)
  if simObj.shared.softcut is not None:
    fort4 += "  softcut= {}\n".format(simObj.shared.softcut)
  if simObj.shared.linit is not None:
    fort4 += "  linit= {}\n".format(su.logicToString(simObj.shared.linit))
  if simObj.shared.lreadq is not None:
    fort4 += "  lreadq= {}\n".format(su.logicToString(simObj.shared.lreadq))
  if simObj.shared.nchain is not None:
    fort4 += "  nchain= {}\n".format(simObj.shared.nchain)

  fort4 += "/ \n\n"

  fort4 += "&analysis\n"

  if simObj.analysis.iprint is not None:
    fort4 += "  iprint= {}\n".format(simObj.analysis.iprint)
  if simObj.analysis.imv is not None:
    fort4 += "  imv= {}\n".format(simObj.analysis.imv)
  if simObj.analysis.iblock is not None:
    fort4 += "  iblock= {}\n".format(simObj.analysis.iblock)
  if simObj.analysis.iratp is not None:
    fort4 += "  iratp= {}\n".format(simObj.analysis.iratp)
  if simObj.analysis.idiele is not None:
    fort4 += "  idiele= {}\n".format(simObj.analysis.idiele)
  if simObj.analysis.iheatcapacity is not None:
    fort4 += "  iheatcapacity= {}\n".format(simObj.analysis.iheatcapacity)
  if simObj.analysis.ianalyze is not None:
    fort4 += "  ianalyze= {}\n".format(simObj.analysis.ianalyze)
  if simObj.analysis.nbin is not None:
    fort4 += "  nbin= {}\n".format(simObj.analysis.nbin)
  if simObj.analysis.lintra is not None:
    fort4 += "  lintra= {}\n".format(su.logicToString(simObj.analysis.lintra))
  if simObj.analysis.lstretch is not None:
    fort4 += "  lstretch= {}\n".format(su.logicToString(simObj.analysis.lstretch))
  if simObj.analysis.lgvst is not None:
    fort4 += "  lgvst= {}\n".format(su.logicToString(simObj.analysis.lgvst))
  if simObj.analysis.lbend is not None:
    fort4 += "  lbend= {}\n".format(su.logicToString(simObj.analysis.lbend))
  if simObj.analysis.lete is not None:
    fort4 += "  lete= {}\n".format(su.logicToString(simObj.analysis.lete))
  if simObj.analysis.lrhoz is not None:
    fort4 += "  lrhoz= {}\n".format(su.logicToString(simObj.analysis.lrhoz))
  if simObj.analysis.lucall is not None:
    fort4 += "  lucall= {}\n".format(su.logicToString(simObj.analysis.lucall))

  fort4 += "/ \n\n"

  fort4 += "&mc_volume\n"

  if simObj.volume.tavol is not None:
    fort4 += "  tavol= {}\n".format(simObj.volume.tavol)
  if simObj.volume.iratv is not None:
    fort4 += "  iratv= {}\n".format(simObj.volume.iratv)
  if simObj.volume.pmvlmt is not None:
    fort4 += "  pmvlmt= {}\n".format(simObj.volume.pmvlmt.unrolledString())
  if simObj.volume.pmvolb is not None:
    fort4 += "  pmvolb= {}\n".format(simObj.volume.pmvolb.unrolledString())
  if simObj.volume.box5 is not None:
    fort4 += "  box5= {}\n".format(simObj.volume.box5.unrolledString())
  if simObj.volume.box6 is not None:
    fort4 += "  box6= {}\n".format(simObj.volume.box6.unrolledString())
  if simObj.volume.pmvol is not None:
    fort4 += "  pmvol= {}\n".format(simObj.volume.pmvol)
  if simObj.volume.pmvolx is not None:
    fort4 += "  pmvolx= {}\n".format(simObj.volume.pmvolx)
  if simObj.volume.pmvoly is not None:
    fort4 += "  pmvoly= {}\n".format(simObj.volume.pmvoly)
  if simObj.volume.rmvolume is not None:
    fort4 += "  rmvolume= {}\n".format(simObj.volume.rmvolume)
  if simObj.volume.allow_cutoff_failure is not None:
    fort4 += "  allow_cutoff_failure= {}\n".format(simObj.volume.allow_cutoff_failure)

  fort4 += "/ \n\n"

  fort4 += "&mc_cbmc\n"

  if simObj.cbmc.rcutin is not None:
    fort4 += "  rcutin= {}\n".format(simObj.cbmc.rcutin)
  if simObj.cbmc.pmcb is not None:
    fort4 += "  pmcb= {}\n".format(simObj.cbmc.pmcb)
  if simObj.cbmc.pmcbmt is not None:
    fort4 += "  pmcbmt= {}\n".format(simObj.cbmc.pmcbmt.unrolledString())
  if simObj.cbmc.pmall is not None:
    fort4 += "  pmall= {}\n".format(simObj.cbmc.pmall.unrolledString())
  if simObj.cbmc.nchoi1 is not None:
    fort4 += "  nchoi1= {}\n".format(simObj.cbmc.nchoi1.unrolledString())
  if simObj.cbmc.nchoi is not None:
    fort4 += "  nchoi= {}\n".format(simObj.cbmc.nchoi.unrolledString())
  if simObj.cbmc.nchoir is not None:
    fort4 += "  nchoir= {}\n".format(simObj.cbmc.nchoir.unrolledString())
  if simObj.cbmc.nchoih is not None:
    fort4 += "  nchoih= {}\n".format(simObj.cbmc.nchoih.unrolledString())
  if simObj.cbmc.nchtor is not None:
    fort4 += "  nchtor= {}\n".format(simObj.cbmc.nchtor.unrolledString())
  if simObj.cbmc.nchbna is not None:
    fort4 += "  nchbna= {}\n".format(simObj.cbmc.nchbna.unrolledString())
  if simObj.cbmc.nchbnb is not None:
    fort4 += "  nchbnb= {}\n".format(simObj.cbmc.nchbnb.unrolledString())
  if simObj.cbmc.icbdir is not None:
    fort4 += "  icbdir= {}\n".format(simObj.cbmc.icbdir.unrolledString())
  if simObj.cbmc.icbsta is not None:
    fort4 += "  icbsta= {}\n".format(simObj.cbmc.icbsta.unrolledString())

  fort4 += "/ \n\n"

  fort4 += "&mc_simple\n"
  if simObj.simple.pm_atom_tra is not None:
    fort4 += "  pm_atom_tra= {}\n".format(simObj.simple.pm_atom_tra)
  if simObj.simple.Armtra is not None:
    fort4 += "  Armtra= {}\n".format(simObj.simple.Armtra.unrolledString())
  if simObj.simple.pmtra is not None:
    fort4 += "  pmtra= {}\n".format(simObj.simple.pmtra)
  if simObj.simple.pmtrmt is not None:
    fort4 += "  pmtrmt= {}\n".format(simObj.simple.pmtrmt.unrolledString())
  if simObj.simple.rmtra is not None:
    fort4 += "  rmtra= {}\n".format(simObj.simple.rmtra.unrolledString())
  if simObj.simple.tatra is not None:
    fort4 += "  tatra= {}\n".format(simObj.simple.tatra)
  if simObj.simple.pmromt is not None:
    fort4 += "  pmromt= {}\n".format(simObj.simple.pmromt.unrolledString())
  if simObj.simple.rmrot is not None:
    fort4 += "  rmrot= {}\n".format(simObj.simple.rmrot.unrolledString())
  if simObj.simple.tarot is not None:
    fort4 += "  tarot= {}\n".format(simObj.simple.tarot)
  fort4 += "/ \n\n"

  fort4 += "&mc_ee\n"
  if simObj.ee.pmexpc is not None:
    fort4 += "  pmexpc= {}\n".format(simObj.ee.pmexpc)
  if simObj.ee.pmeemt is not None:
    fort4 += "  pmeemt= {}\n".format(simObj.ee.pmeemt.unrolledString())
  if simObj.ee.pmexpc1 is not None:
    fort4 += "  pmexpc1= {}\n".format(simObj.ee.pmexpc1)
  if simObj.ee.lexpand is not None:
    fort4 += "  lexpand= {}\n".format(simObj.ee.lexpand.unrolledString())
  fort4 += f"/ \n\n"

  fort4 += "&external_field\n"
  if simObj.external_field.Elect_field is not None:
    fort4 += "  Elect_field= {}\n".format(simObj.external_field.Elect_field)
  fort4 += f"/ \n\n"

  fort4 += "&mc_flucq\n"
  if simObj.flucq.taflcq is not None:
    fort4 += "  taflcq= {}\n".format(simObj.flucq.taflcq)
  if simObj.flucq.fqtemp is not None:
    fort4 += "  fqtemp= {}\n".format(simObj.flucq.fqtemp)
  if simObj.flucq.rmflucq is not None:
    fort4 += "  rmflucq= {}\n".format(simObj.flucq.rmflucq)
  if simObj.flucq.pmflcq is not None:
    fort4 += "  pmflcq= {}\n".format(simObj.flucq.pmflcq)
  if simObj.flucq.pmfqmt is not None:
    fort4 += "  pmfqmt= {}\n".format(simObj.flucq.pmfqmt.unrolledString())
  if simObj.flucq.lflucq is not None:
    fort4 += "  lflucq= {}\n".format(simObj.flucq.lflucq.unrolledString())
  if simObj.flucq.lqtrans is not None:
    fort4 += "  lqtrans= {}\n".format(simObj.flucq.lqtrans.unrolledString())
  if simObj.flucq.fqegp is not None:
    fort4 += "  fqegp= {}\n".format(simObj.flucq.fqegp.unrolledString())
  if simObj.flucq.nchoiq is not None:
    fort4 += "  nchoiq= {}\n".format(simObj.flucq.nchoiq.unrolledString())
  if simObj.flucq.nswapq is not None:
    fort4 += "  nswapq= {}\n".format(simObj.flucq.nswapq)
  fort4 += f"/ \n\n"

  fort4 += "&mc_gcmc\n"
  if simObj.gcmc.nequil is not None:
    fort4 += "  nequil= {}\n".format(simObj.gcmc.nequil)
  if simObj.gcmc.ninstf is not None:
    fort4 += "  ninstf= {}\n".format(simObj.gcmc.ninstf)
  if simObj.gcmc.ninsth is not None:
    fort4 += "  ninsth= {}\n".format(simObj.gcmc.ninsth)
  if simObj.gcmc.ndumph is not None:
    fort4 += "  ndumph= {}\n".format(simObj.gcmc.ndumph)
  if simObj.gcmc.B is not None:
    fort4 += "  B= {}\n".format(simObj.gcmc.B.unrolledString())
  fort4 += f"/ \n\n"

  fort4 += "&mc_swatch\n"
  if simObj.swatch.pmswat is not None:
    fort4 += "  pmswat= {}\n".format(simObj.swatch.pmswat)
  if simObj.swatch.nswaty is not None:
    fort4 += "  nswaty= {}\n".format(simObj.swatch.nswaty)
  if simObj.swatch.pmsatc is not None:
    fort4 += "  pmsatc= {}\n".format(simObj.swatch.pmsatc.unrolledString())
  fort4 += f"/ \n\n"

  fort4 += "SIMULATION_BOX\n"

  if simObj.boxes is not None:
    for i in range(simObj.boxes.length):
      box = simObj.boxes[i+1]
      fort4 += "{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
        box.boxlx, box.boxly, box.boxlz, 
        box.rcut, box.kalp, box.rcutnn, box.numDimIso,
        su.logicToString(box.lsolid), su.logicToString(box.lrect), su.logicToString(box.lideal),
        su.logicToString(box.ltwice), box.T, box.P
      )
      fort4 += "{} {}\n".format(box.nchain_mt.unrolledString(), box.ghost_particles)
      fort4 += "{} {} {} {} {} {} {} {} {}\n".format(box.inix, box.iniy, box.iniz, box.inirot, 
                box.inimix, box.zshift, box.dshift, su.logicToString(box.use_linkcell), box.rintramax) 

  fort4 += "END SIMULATION_BOX\n\n\n"

  fort4 += "MOLECULE_TYPE\n"

  if simObj.mtypes is not None:
    for i in range(simObj.mtypes.length):
      mtype = simObj.mtypes[i+1]
      fort4 += "{} {} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(mtype.nunit, mtype.nugrow,
                mtype.ncarbon, mtype.maxcbmc, mtype.maxgrow, mtype.iring, su.logicToString(mtype.lelect),
                su.logicToString(mtype.lring), su.logicToString(mtype.lrigid), 
                su.logicToString(mtype.lbranch), su.logicToString(mtype.lsetup),
                su.logicToString(mtype.lq14scale), mtype.qscale, mtype.iurot, mtype.isolute)

      for j in range(mtype.nunit):

        bead = mtype.beads[j+1]

        fort4 += "{} {} {}\n".format(bead.unit, bead.ntype, bead.leaderq)

        if bead.nbonds is not None:
          fort4 += "{}\n".format(bead.nbonds)
          for k in range(bead.nbonds):
            bb = bead.bonds[k+1]
            fort4 += "{} {}\n".format(bb.junit, bb.bondID)
        else:
          fort4 += "0\n"
       
        if bead.angles is not None:
          fort4 += "{}\n".format(bead.nangles)
          for k in range(bead.nangles):
            ba = bead.angles[k+1]
            fort4 += "{} {} {}\n".format(ba.junit, ba.kunit, ba.angleID)
        else:
          fort4 += "0\n"

        if bead.dihedrals is not None:
          fort4 += "{}\n".format(bead.ndihedrals)
          for k in range(bead.ndihedrals):
            bd = bead.dihedrals[k+1]
            fort4 += "{} {} {} {}\n".format(bd.junit, bd.kunit, bd.lunit,  bd.dihedralID)
        else:
          fort4 += "0\n"

  fort4 += "END MOLECULE_TYPE\n\n\n"

  fort4 += "MC_SWAP\n"

  if simObj.swap_table:
    for i in range(simObj.swap_table.length):
      stab = simObj.swap_table[i+1]
      fort4 += "{} {}\n".format(stab.nswapb, stab.pmswapb.unrolledString())
      for j in range(stab.nswapb):
        fort4 += "{} {}\n".format(stab.boxPairs[j+1][0], stab.boxPairs[j+1][1])
  
  fort4 += "END MC_SWAP\n\n\n"

  fort4 += "MC_SWATCH\n"
  fort4 += "END MC_SWATCH\n\n\n"

# SWATCH table not yet supported (nswaty must be 0)
#  if simObj.swatch_table:
#    for i in range(simObj.swatch_table.length):
#      stab = simObj.swatch_table[i+1]

  with open(fort4File,"w") as f:
    f.write(fort4)
