import { Link } from "react-router-dom";
import Video from "../../videos/video.mp4";
import {
  HeroContainer,
  HeroBg,
  VideoBg,
  HeroContent,
  HeroH1,
  HeroP,
  HeroBtnWrapper,
} from "./HeroElements";

function HeroSection() {

  return (
    <HeroContainer id="home">
      <HeroBg>
        <VideoBg playsInline autoPlay loop muted src={Video} type="video/mp4" />
      </HeroBg>
      <HeroContent>
        <HeroH1>Garden Palooza</HeroH1>
        <HeroP>
          Discover, collect and grow lovely plants and expand your garden!
        </HeroP>
        <HeroBtnWrapper>
           <Link to="/guest">Guest Login</Link>
        </HeroBtnWrapper>
      </HeroContent>
    </HeroContainer>
  );
}

export default HeroSection;
