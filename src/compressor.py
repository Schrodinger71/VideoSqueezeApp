import ffmpeg

def compress_video(input_file, output_file, crf=28):
    try:
        ffmpeg.input(input_file).output(output_file, vcodec='libx264', crf=crf).run(overwrite_output=True)
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg error: {e.stderr.decode()}")
