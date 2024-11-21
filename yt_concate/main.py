from pipeline.pipeline import Pipeline
from pipeline.steps.get_vedio_list import GetVedioList
CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"

def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVedioList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)

if __name__ == '__main__':
    main()

