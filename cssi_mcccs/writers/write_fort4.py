from cssi_mcccs.utilities import string_util as su

def write_fort4(simObj,fort4File="fort.4"):

  fort4 = ""

  fort4 += "&mc_shared\n"

  fort4 += "/ \n\n"

  fort4 += "&analysis\n"

  fort4 += "/ \n\n"

  fort4 += "&external_field\n"

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

  fort4 += "SIMULATION_BOX\n"

  if simObj.boxes is not None:
    for i in range(simObj.boxes.length):
      box = simObj.boxes[i+1]
      fort4 += "{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(box.boxlx, box.boxly, box.boxlz, 
                box.rcut, box.kalp, box.rcutnn, box.numDimensionIsIsotropic,
                su.logicToString(box.lsolid), su.logicToString(box.lrect), su.logicToString(box.lideal),
                su.logicToString(box.ltwice), box.temperature, box.pressure)
      fort4 += "{}\n".format(box.nchain_mt.unrolledString())
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
            fort4 += "{} {}\n".format(ba.junit, ba.kunit, ba.angleID)
        else:
          fort4 += "0\n"

        if bead.dihedrals is not None:
          fort4 += "{}\n".format(bead.ndihedrals)
          for k in range(bead.ndihedrals):
            bd = bead.dihedrals[k+1]
            fort4 += "{} {}\n".format(bd.junit, bd.kunit, bd.lunit,  bd.dihedralID)
        else:
          fort4 += "0\n"

  fort4 += "END MOLECULE_TYPE\n"

  with open(fort4File,"w") as f:
    f.write(fort4)
