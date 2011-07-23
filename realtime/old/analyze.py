#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Analyze
# Generated: Sun Jul 10 15:41:33 2011
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class analyze(gr.top_block):

	def __init__(self, infile="data", samp_rate=1000000, outfile="data.wav", amp=70):
		gr.top_block.__init__(self, "Analyze")

		##################################################
		# Parameters
		##################################################
		self.infile = infile
		self.samp_rate = samp_rate
		self.outfile = outfile
		self.amp = amp

		##################################################
		# Blocks
		##################################################
		self.gr_wavfile_sink_0 = gr.wavfile_sink(outfile, 3, samp_rate, 16)
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vcc((amp, ))
		self.gr_file_source_0 = gr.file_source(gr.sizeof_gr_complex*1, infile, False)
		self.gr_complex_to_mag_0 = gr.complex_to_mag(1)
		self.gr_complex_to_float_0 = gr.complex_to_float(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.gr_complex_to_float_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.gr_complex_to_mag_0, 0))
		self.connect((self.gr_complex_to_mag_0, 0), (self.gr_wavfile_sink_0, 2))
		self.connect((self.gr_complex_to_float_0, 1), (self.gr_wavfile_sink_0, 1))
		self.connect((self.gr_complex_to_float_0, 0), (self.gr_wavfile_sink_0, 0))

	def get_infile(self):
		return self.infile

	def set_infile(self, infile):
		self.infile = infile

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

	def get_outfile(self):
		return self.outfile

	def set_outfile(self, outfile):
		self.outfile = outfile

	def get_amp(self):
		return self.amp

	def set_amp(self, amp):
		self.amp = amp
		self.gr_multiply_const_vxx_0.set_k((self.amp, ))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("-i", "--infile", dest="infile", type="string", default="data",
		help="Set Input File [default=%default]")
	parser.add_option("-s", "--samp-rate", dest="samp_rate", type="long", default=1000000,
		help="Set Sample Rate [default=%default]")
	parser.add_option("-o", "--outfile", dest="outfile", type="string", default="data.wav",
		help="Set Output File [default=%default]")
	parser.add_option("-a", "--amp", dest="amp", type="complex", default=70,
		help="Set Amplification [default=%default]")
	(options, args) = parser.parse_args()
	tb = analyze(infile=options.infile, samp_rate=options.samp_rate, outfile=options.outfile, amp=options.amp)
	tb.run()

