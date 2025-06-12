# 日志记录格式
LOG_FORMAT = {
    "timestamp": "05-14 11:10:23",
    "level": "INFO",
    "file": "logger.py",
    "line": 37,
    "request_id": "chatcmpl-bc5db8a1022b4ae88862cc7f5186f2c1",
    "content": {
        "prompt": {
            "system": "As an advanced reading comprehension assistant, your task is to analyze text passages and corresponding questions meticulously. Your response start after \"Thought: \", where you will methodically break down the reasoning process, illustrating how you arrive at conclusions. Conclude with \"Answer: \" to present a concise, definitive response, devoid of additional elaborations.",
            "user": [
                {
                    "title": "The Last Horse",
                    "content": "The Last Horse (Spanish:El último caballo) is a 1950 Spanish comedy film directed by Edgar Neville starring Fernando Fernán Gómez."
                },
                {
                    "title": "Southampton",
                    "content": "The University of Southampton, which was founded in 1862 and received its Royal Charter as a university in 1952, has over 22,000 students..."
                },
                {
                    "title": "Stanton Township, Champaign County, Illinois",
                    "content": "Stanton Township is a township in Champaign County, Illinois, USA. As of the 2010 census, its population was 505 and it contained 202 housing units."
                },
                {
                    "title": "Neville A. Stanton",
                    "content": "Neville A. Stanton is a British Professor of Human Factors and Ergonomics at the University of Southampton..."
                },
                {
                    "title": "Finding Nemo",
                    "content": "Finding Nemo Theatrical release poster Directed by Andrew Stanton..."
                }
            ],
            "question": "When was Neville A. Stanton's employer founded?",
            "assistant": {
                "thought": "The employer of Neville A. Stanton is University of Southampton. The University of Southampton was founded in 1862.",
                "answer": "1862"
            }
        },
        "parameters": {
            "n": 1,
            "presence_penalty": 0.0,
            "frequency_penalty": 0.0,
            "repetition_penalty": 1.0,
            "temperature": 0.0,
            "top_p": 1.0,
            "top_k": -1,
            "min_p": 0.0,
            "seed": None,
            "stop": [],
            "stop_token_ids": [],
            "bad_words": [],
            "include_stop_str_in_output": False,
            "ignore_eos": False,
            "max_tokens": 2048,
            "min_tokens": 0,
            "logprobs": None,
            "prompt_logprobs": None,
            "skip_special_tokens": True,
            "spaces_between_special_tokens": True,
            "truncate_prompt_tokens": None,
            "guided_decoding": None
        },
        "additional_info": {
            "prompt_token_ids": None,
            "lora_request": None,
            "prompt_adapter_request": None
        }
    }
}