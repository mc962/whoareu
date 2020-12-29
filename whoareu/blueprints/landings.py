from dataclasses import dataclass
from functools import cached_property
from ipaddress import ip_address

from flask import Blueprint, render_template, request, jsonify
from werkzeug.useragents import UserAgent

blueprint = Blueprint('landings', __name__, url_prefix='/')


@blueprint.route('', methods=['GET'])
def home() -> str:
    info = UserInfo(
        user_agent=request.user_agent,
        ip_address=request.remote_addr,
        language=request.accept_languages.best,
        referer=request.referrer,
        method=request.method,
    )

    return render_template('landings/home.html', request_info=info)


@blueprint.route('/ping', methods=['GET', 'HEAD'])
def ping() -> str:
    return jsonify(alternative_ip_address=request.remote_addr)


@dataclass(frozen=True)
class UserInfo:
    PLATFORMS_DISPLAY = {
        'macos': 'MacOS'
    }

    LANGUAGES_DISPLAY = {
        'en-US': 'American English'
    }

    user_agent: UserAgent
    ip_address: str
    language: str
    referer: str
    method: str

    def browser(self) -> str:
        if self.user_agent:
            return self.user_agent.browser.capitalize()
        else:
            return ''

    def platform(self) -> str:
        if self.user_agent:
            return UserInfo.PLATFORMS_DISPLAY.get(self.user_agent.platform) or self.user_agent.platform.capitalize()
        else:
            return ''

    def version(self) -> str:
        if self.version:
            return self.user_agent.version
        else:
            return ''

    def display_language(self) -> str:
        humanized_language = UserInfo.LANGUAGES_DISPLAY.get(self.language)
        if humanized_language:
            display = f'{humanized_language} ({self.language})'
        else:
            display = self.language

        return display

    @cached_property
    def ip_version(self) -> str:
        return ip_address(self.ip_address).version

    @cached_property
    def alternative_ip_version(self) -> str:
        if self.ip_version == 4:
            return '6'
        else:
            return '4'
