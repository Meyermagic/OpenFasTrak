#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Replay
# Generated: Sun Jul 10 15:41:36 2011
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class replay(gr.top_block):

	def __init__(self, infile="data", samp_rate=1000000):
		gr.top_block.__init__(self, "Replay")

		##################################################
		# Parameters
		##################################################
		self.infile = infile
		self.samp_rate = samp_rate

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="",
			io_type=uhd.io_type.COMPLEX_FLOAT32,
			num_channels=1,
		)
		self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
		self.uhd_usrp_sink_0.set_center_freq(915000000, 0)
		self.uhd_usrp_sink_0.set_gain(0, 0)
		self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
		self.gr_file_source_0 = gr.file_source(gr.sizeof_gr_complex*1, infile, False)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.uhd_usrp_sink_0, 0))

	def get_infile(self):
		return self.infile

	def set_infile(self, infile):
		self.infile = infile

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("-i", "--infile", dest="infile", type="string", default="data",
		help="Set Input File [default=%default]")
	parser.add_option("-s", "--samp-rate", dest="samp_rate", type="long", default=1000000,
		help="Set Sample Rate [default=%default]")
	(options, args) = parser.parse_args()
	tb = replay(infile=options.infile, samp_rate=options.samp_rate)
	tb.run()

