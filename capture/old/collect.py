#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Collect
# Generated: Sun Jul 10 15:41:38 2011
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class collect(gr.top_block):

	def __init__(self, outfile="data", samp_rate=1000000):
		gr.top_block.__init__(self, "Collect")

		##################################################
		# Parameters
		##################################################
		self.outfile = outfile
		self.samp_rate = samp_rate

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			io_type=uhd.io_type.COMPLEX_FLOAT32,
			num_channels=1,
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(915000000, 0)
		self.uhd_usrp_source_0.set_gain(0, 0)
		self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_gr_complex*1, outfile)
		self.gr_file_sink_0.set_unbuffered(False)

		##################################################
		# Connections
		##################################################
		self.connect((self.uhd_usrp_source_0, 0), (self.gr_file_sink_0, 0))

	def get_outfile(self):
		return self.outfile

	def set_outfile(self, outfile):
		self.outfile = outfile

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("-o", "--outfile", dest="outfile", type="string", default="data",
		help="Set Output File [default=%default]")
	parser.add_option("-s", "--samp-rate", dest="samp_rate", type="long", default=1000000,
		help="Set Sample Rate [default=%default]")
	(options, args) = parser.parse_args()
	tb = collect(outfile=options.outfile, samp_rate=options.samp_rate)
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()

