# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ragout(PythonPackage):
    """Ragout (Reference-Assisted Genome Ordering UTility) is a tool
    for chromosome-level scaffolding using multiple references.
    Given initial assembly fragments (contigs/scaffolds)
    and one or multiple related references (complete or draft)
    it produces a chromosome-scale assembly (as a set of scaffolds).
    """

    homepage = "https://github.com/fenderglass/Ragout"
    url      = "https://github.com/fenderglass/Ragout/archive/2.3.tar.gz"

    version('2.3', sha256='69d50a7ff49f03821e0143449ee0dc3e80c73e2c24568cad71948a5492613bca')

    depends_on('py-setuptools')
    depends_on('hal')
    depends_on('py-networkx')
