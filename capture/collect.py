#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Collect
# Generated: Thu Jul 21 17:36:55 2011
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class collect(gr.top_block):

	def __init__(self, audio_pass=5000, audio_stop=5500, threshold_mag=0.25, low_pass_transition_width=1000, freq_offset=1000000, outfile="datafifo", samp_rate=64000000, low_pass_offset=100):
		gr.top_block.__init__(self, "Collect")

		##################################################
		# Parameters
		##################################################
		self.audio_pass = audio_pass
		self.audio_stop = audio_stop
		self.threshold_mag = threshold_mag
		self.low_pass_transition_width = low_pass_transition_width
		self.freq_offset = freq_offset
		self.outfile = outfile
		self.samp_rate = samp_rate
		self.low_pass_offset = low_pass_offset

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			io_type=uhd.io_type.COMPLEX_FLOAT32,
			num_channels=1,
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(915000000 - freq_offset, 0)
		self.uhd_usrp_source_0.set_gain(0, 0)
		self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
		self.low_pass_filter_0 = gr.fir_filter_ccf(1, firdes.low_pass(
			2, samp_rate, freq_offset+low_pass_offset, low_pass_transition_width, firdes.WIN_HAMMING, 6.76))
		self.gr_threshold_ff_0 = gr.threshold_ff(-threshold_mag, threshold_mag, 0)
		self.gr_float_to_char_0 = gr.float_to_char()
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_char*1, outfile)
		self.gr_file_sink_0.set_unbuffered(False)
		self.gr_agc2_xx_0 = gr.agc2_cc(1e-1, 1e-2, 1.0, 1.0, 0.0)
		self.blks2_am_demod_cf_0 = blks2.am_demod_cf(
			channel_rate=samp_rate,
			audio_decim=1,
			audio_pass=5000,
			audio_stop=5500,
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.low_pass_filter_0, 0), (self.blks2_am_demod_cf_0, 0))
		self.connect((self.gr_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.gr_agc2_xx_0, 0))
		self.connect((self.blks2_am_demod_cf_0, 0), (self.gr_threshold_ff_0, 0))
		self.connect((self.gr_threshold_ff_0, 0), (self.gr_float_to_char_0, 0))
		self.connect((self.gr_float_to_char_0, 0), (self.gr_file_sink_0, 0))

	def get_audio_pass(self):
		return self.audio_pass

	def set_audio_pass(self, audio_pass):
		self.audio_pass = audio_pass

	def get_audio_stop(self):
		return self.audio_stop

	def set_audio_stop(self, audio_stop):
		self.audio_stop = audio_stop

	def get_threshold_mag(self):
		return self.threshold_mag

	def set_threshold_mag(self, threshold_mag):
		self.threshold_mag = threshold_mag
		self.gr_threshold_ff_0.set_hi(self.threshold_mag)
		self.gr_threshold_ff_0.set_lo(-self.threshold_mag)

	def get_low_pass_transition_width(self):
		return self.low_pass_transition_width

	def set_low_pass_transition_width(self, low_pass_transition_width):
		self.low_pass_transition_width = low_pass_transition_width
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.freq_offset+self.low_pass_offset, self.low_pass_transition_width, firdes.WIN_HAMMING, 6.76))

	def get_freq_offset(self):
		return self.freq_offset

	def set_freq_offset(self, freq_offset):
		self.freq_offset = freq_offset
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.freq_offset+self.low_pass_offset, self.low_pass_transition_width, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_center_freq(915000000 - self.freq_offset, 0)

	def get_outfile(self):
		return self.outfile

	def set_outfile(self, outfile):
		self.outfile = outfile

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.freq_offset+self.low_pass_offset, self.low_pass_transition_width, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

	def get_low_pass_offset(self):
		return self.low_pass_offset

	def set_low_pass_offset(self, low_pass_offset):
		self.low_pass_offset = low_pass_offset
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.freq_offset+self.low_pass_offset, self.low_pass_transition_width, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--audio-pass", dest="audio_pass", type="eng_float", default=eng_notation.num_to_str(5000),
		help="Set Audio Pass [default=%default]")
	parser.add_option("", "--audio-stop", dest="audio_stop", type="eng_float", default=eng_notation.num_to_str(5500),
		help="Set Audio Stop [default=%default]")
	parser.add_option("-m", "--threshold-mag", dest="threshold_mag", type="eng_float", default=eng_notation.num_to_str(0.25),
		help="Set Threshold Magnitude [default=%default]")
	parser.add_option("-w", "--low-pass-transition-width", dest="low_pass_transition_width", type="eng_float", default=eng_notation.num_to_str(1000),
		help="Set Low Pass Transition Width [default=%default]")
	parser.add_option("-f", "--freq-offset", dest="freq_offset", type="eng_float", default=eng_notation.num_to_str(1000000),
		help="Set Frequency Offset [default=%default]")
	parser.add_option("-o", "--outfile", dest="outfile", type="string", default="datafifo",
		help="Set Output File (a named pipe) [default=%default]")
	parser.add_option("-s", "--samp-rate", dest="samp_rate", type="long", default=64000000,
		help="Set Sample Rate [default=%default]")
	parser.add_option("-l", "--low-pass-offset", dest="low_pass_offset", type="eng_float", default=eng_notation.num_to_str(100),
		help="Set Low Pass Offset [default=%default]")
	(options, args) = parser.parse_args()
	tb = collect(audio_pass=options.audio_pass, audio_stop=options.audio_stop, threshold_mag=options.threshold_mag, low_pass_transition_width=options.low_pass_transition_width, freq_offset=options.freq_offset, outfile=options.outfile, samp_rate=options.samp_rate, low_pass_offset=options.low_pass_offset)
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()

