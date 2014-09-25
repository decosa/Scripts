#!/usr/bin/env python
import ROOT
import DataFormats.FWLite as fwlite #import Events, Handle
import sys
import optparse

if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    (opt, args) = parser.parse_args()

    sys.argv.append('-b')
    ROOT.gROOT.SetBatch()        # don't pop up canvases

    fileName = args[0]

    events = fwlite.Events( fileName )

    # create handleEl outside of loop
    handleLHE = fwlite.Handle('LHEEventProduct')
    handleGens = fwlite.Handle("std::vector<reco::GenParticle>")


    # a label is just a tuple of strings that is initialized just
    # like and edm::InputTag
    #labelGens = ('prunedGenParticles')
    labelGens = ('genParticles')



    for event in events:

	event.getByLabel(labelGens,handleGens)
	gens = handleGens.product()
        for gg in xrange(len(gens)):
            #            print gens[gg].pdgId()
            #print gens[gg].mother(0).pdgId()
            print "Original particle"
            print type(gens[gg])
            print "Mother ID"
            mom = gens[gg].mother()
            print gens[gg].numberOfMothers()
            #print dir(mom)
            if(gens[gg].numberOfMothers() !=0): print mom.px()

            #            print type(gens[gg].mother())
